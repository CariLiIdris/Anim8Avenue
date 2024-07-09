from flask import jsonify, request, session, send_from_directory   # type: ignore
from werkzeug.utils import secure_filename # type: ignore
import os
from models.user import User
from models.message import Message
from server import app

UPLOAD_FOLDER = 'uploads/'  # Define your upload folder
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
  os.makedirs(UPLOAD_FOLDER)

@app.route('/api/messages', methods=['POST'])
def send_message():
  if 'userID' not in session:
      return jsonify({'error': 'Unauthorized'}), 401

  sender_id = session['userID']
  recipient_id = request.form.get('recipient_id')
  message_content = request.form.get('message')

  data = {
      'sender_id': sender_id,
      'recipient_id': recipient_id,
      'message': message_content
  }

  file = request.files.get('file')
  if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      
      # Ensure the directory exists before saving the file
      if not os.path.exists(app.config['UPLOAD_FOLDER']):
          os.makedirs(app.config['UPLOAD_FOLDER'])
      
      file.save(file_path)
      data['file'] = file_path
  else:
      data['file'] = None

  if not Message.validate_message(data):
      return jsonify({'error': 'Invalid message'}), 400

  Message.send_message(data)
  return jsonify({'message': 'Message sent'}), 201

@app.route('/api/messages/<int:recipient_id>', methods=['GET'])
def get_messages(recipient_id):
  if 'userID' not in session:
      return jsonify({'error': 'Unauthorized'}), 401

  user_id = session['userID']
  messages = Message.get_messages_between_users(user_id, recipient_id)
  return jsonify([message.to_dict() for message in messages]), 200

@app.route('/api/messages', methods=['GET'])
def get_user_messages():
  if 'userID' not in session:
      return jsonify({'error': 'Unauthorized'}), 401

  user_id = session['userID']
  messages = User.getUserMessages(user_id)
  return jsonify([message.to_dict() for message in messages]), 200

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
  return send_from_directory(app.config['UPLOAD_FOLDER'], filename)