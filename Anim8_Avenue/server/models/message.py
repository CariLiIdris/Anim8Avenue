from config.mysqlconnection import connectToMySQL
from flask import flash # type: ignore
import os
import datetime

class Message:
  from config import DB

  def __init__(self, data):
    self._id = data['_id']
    self.sender_id = data['sender_id']
    self.sender_username = data.get('sender_username')
    self.sender_fName = data.get('sender_fName')
    self.sender_lName = data.get('sender_lName')
    self.sender_email = data.get('sender_email')
    self.recipient_id = data['recipient_id']
    self.recipient_username = data.get('recipient_username')
    self.recipient_fName = data.get('recipient_fName')
    self.recipient_lName = data.get('recipient_lName')
    self.recipient_email = data.get('recipient_email')
    self.message = data['message']
    self.file = data.get('file')
    self.created_at = data['created_at']

  def to_dict(self):
    return {
        '_id': self._id,
        'sender_id': self.sender_id,
        'sender_username': self.sender_username,
        'sender_fName': self.sender_fName,
        'sender_lName': self.sender_lName,
        'sender_email': self.sender_email,
        'recipient_id': self.recipient_id,
        'recipient_username': self.recipient_username,
        'recipient_fName': self.recipient_fName,
        'recipient_lName': self.recipient_lName,
        'recipient_email': self.recipient_email,
        'message': self.message,
        'file': self.file,
        'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
      }

  @classmethod
  def send_message(cls, data):
    query = '''
            INSERT INTO messages (sender_id, recipient_id, message, file)
            VALUES (%(sender_id)s, %(recipient_id)s, %(message)s, %(file)s);
            '''
    return connectToMySQL(cls.DB).query_db(query, data)

  @classmethod
  def get_messages_between_users(cls, user1_id, user2_id):
    query = '''
            SELECT messages.*, 
                    sender.username AS sender_username, 
                    sender.fName AS sender_fName,
                    sender.lName AS sender_lName,
                    sender.email AS sender_email,
                    recipient.username AS recipient_username, 
                    recipient.fName AS recipient_fName,
                    recipient.lName AS recipient_lName,
                    recipient.email AS recipient_email
            FROM messages
            LEFT JOIN users AS sender ON messages.sender_id = sender._id
            LEFT JOIN users AS recipient ON messages.recipient_id = recipient._id
            WHERE (sender_id = %(user1_id)s AND recipient_id = %(user2_id)s)
            OR (sender_id = %(user2_id)s AND recipient_id = %(user1_id)s)
            ORDER BY created_at;
            '''
    data = {
        'user1_id': user1_id,
        'user2_id': user2_id
    }
    results = connectToMySQL(cls.DB).query_db(query, data)
    return [cls(message) for message in results]

  @classmethod
  def get_messages_for_user(cls, user_id):
    query = '''
            SELECT messages.*, 
                    sender.username AS sender_username, 
                    sender.fName AS sender_fName,
                    sender.lName AS sender_lName,
                    sender.email AS sender_email,
                    recipient.username AS recipient_username, 
                    recipient.fName AS recipient_fName,
                    recipient.lName AS recipient_lName,
                    recipient.email AS recipient_email
            FROM messages
            LEFT JOIN users AS sender ON messages.sender_id = sender._id
            LEFT JOIN users AS recipient ON messages.recipient_id = recipient._id
            WHERE recipient_id = %(user_id)s
            ORDER BY created_at DESC;
            '''
    data = {'user_id': user_id}
    results = connectToMySQL(cls.DB).query_db(query, data)
    return [cls(message) for message in results]

  @staticmethod
  def validate_message(data):
    isValid = True
    message = data.get('message', '')  # Provide a default empty string if 'message' is None
    file = data.get('file', '')  # Provide a default empty string if 'file' is None
    
    if not message and not file:
        flash("Message cannot be empty.", 'error')
        isValid = False
    
    return isValid