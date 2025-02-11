from config.mysqlconnection import connectToMySQL
from flask import flash # type: ignore
import re
import bcrypt # type: ignore

# Email format regex
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# User class
class User:
  from config import DB
  def __init__(self, data):
    self._id = data['_id']
    self.username = data['username']
    self.fName = data['fName']
    self.lName = data['lName']
    self.email = data['email']
    self.password = data['password']
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]

    self.friends = []
    self.groups = []
    self.shows = []
    # self.messages = []

  def to_dict(self):
        return {
            '_id': self._id,
            'username': self.username,
            'fName': self.fName,
            'lName': self.lName,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'friends': [friend.to_dict() for friend in self.friends],
            'groups': [group.to_dict() for group in self.groups],
            'shows': [show.to_dict() for show in self.shows],
            # 'messages': self.messages
        }

# C
  @classmethod
  def createUser(cls, data):
    # create a new user
    hashed_pw = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    data['password'] = hashed_pw
    query = '''
            INSERT INTO users (username, fName, lName, email, password)
            VALUES (
                    %(username)s,
                    %(fName)s,
                    %(lName)s,
                    %(email)s,
                    %(password)s
                  );
            '''
    return connectToMySQL(cls.DB).query_db(query, data)

# R
  @classmethod
  def getAllUsers(cls):
    query = '''
              SELECT * FROM users;
            '''
    results = connectToMySQL(cls.DB).query_db(query)
    users = [cls(user) for user in results]
    return users
  
  # Get user by ID
  @classmethod
  def getUserByID(cls, userID):
    query = '''
              SELECT * FROM users
              WHERE _id = %(_id)s;
            '''
    data = { '_id': userID }
    result = connectToMySQL(cls.DB).query_db(query, data)
    if result:
      user = cls(result[0])
      user.friends = cls.getUserFriends(user._id)
      user.groups = cls.getUserGroups(user._id)
      user.shows = cls.getUserShows(user._id)
      return user
    return None
    
  # Get user by username
  @classmethod
  def getUserByUsername(cls, username):
    query = '''
              SELECT * from users
              WHERE users.username = %(username)s;
            '''
    data = { 'username': username }
    result = connectToMySQL(cls.DB).query_db(query, data)
    if result:
      return cls(result[0])
    return False
  
  # Get user by username
  @classmethod
  def getUserByEmail(cls, email):
    query = '''
              SELECT * from users
              WHERE users.email = %(email)s;
            '''
    data = { 'email': email }
    result = connectToMySQL(cls.DB).query_db(query, data)
    if result:
      return cls(result[0])
    return False

  @classmethod
  def getUserGroups(cls, userID):
    from models.group import Group
    query = '''
            SELECT `groups`.* FROM `groups`
            LEFT JOIN users ON `groups`.owner_id = users._id
            WHERE users._id = %(_id)s;
            '''
    data = {'_id': userID}
    try:
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results:
            return [Group(group) for group in results]
        else:
            return []
    except Exception as e:
        print(f"Error executing query: {e}")
        return []

  @classmethod
  def getUserShows(cls, userID):
    from models.show import Show
    query = '''
            SELECT shows.* FROM shows
            LEFT JOIN users ON shows.owner_id = users._id
            WHERE users._id = %(_id)s;
            '''
    data = {'_id': userID}
    try:
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results:
            return [Show(show) for show in results]
        else:
            return []
    except Exception as e:
        print(f"Error executing query: {e}")
        return []
  
  # U
  @classmethod
  def updateUserByID(cls, userID, data):
    query = '''
              UPDATE users
              SET username=%(username)s, fName=%(fName)s, lName=%(lName)s, email=%(email)s
              WHERE _id = %(_id)s;
            '''
    data['_id'] = userID
    # print("```User.py```",'Data:', data)
    return connectToMySQL(cls.DB).query_db(query, data)
  
  # D
  @classmethod
  def deleteUserByID(cls, userID):
    query = '''
              DELETE FROM users 
              WHERE _id = %(_id)s;
            '''
    data = {'_id': userID}
    return connectToMySQL(cls.DB).query_db(query, data)
  
  @classmethod
  def getUserFriends(cls, userID):
    query = '''
            SELECT users.* FROM users
            LEFT JOIN friends ON users._id = friends.friend_id OR users._id = friends.user_id
            WHERE (friends.user_id = %(_id)s OR friends.friend_id = %(_id)s)
            AND users._id != %(_id)s;
            '''
    data = {'_id': userID}
    try:
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results:
            return [cls(friend) for friend in results]
        else:
            return []
    except Exception as e:
        print(f"Error executing query: {e}")
        return []

  @classmethod
  def addFriend(cls, user_id, friend_id):
    query = '''
            INSERT INTO friends (user_id, friend_id)
            VALUES (
              %(user_id)s, 
              %(friend_id)s
            );
            '''
    data = {'user_id': user_id, 'friend_id': friend_id}
    return connectToMySQL(cls.DB).query_db(query, data)

  @classmethod
  def getUserIDByUsername(cls, username):
    query = '''
            SELECT _id FROM users
            WHERE username = %(username)s;
            '''
    data = {'username': username}
    result = connectToMySQL(cls.DB).query_db(query, data)
    if result:
        return result[0]['_id']
    return None

  @classmethod
  def removeFriend(cls, user_id, friend_id):
    query = '''
            DELETE FROM friends
            WHERE user_id = %(user_id)s AND friend_id = %(friend_id)s;
            '''
    data = {'user_id': user_id, 'friend_id': friend_id}
    return connectToMySQL(cls.DB).query_db(query, data)
  
  # User validations
  @staticmethod
  def validateNewUser(userData):
    isValid = True

    if User.getUserByUsername(userData['username']):
        flash('Username already taken', 'register')
        isValid = False

    if User.getUserByEmail(userData['email']):
        flash('Email already registered', 'register')
        isValid = False

    if len(userData['username']) < 2:
      flash('Username must be greater than 2 characters', 'register')
      isValid = False
    
    if len(userData['fName']) < 2:
      flash('First Name must be at least 2 characters.', 'register')
      isValid = False

    if len(userData['lName']) < 2:
      flash('Last name must be at least than 2 characters.', 'register')
      isValid = False

    if not EMAIL_REGEX.match(userData['email']):
      flash('Invalid email format', 'register')
      isValid = False

    if userData['password'] != userData['confirmPassword']:
      flash('Passwords do not match', 'register')
      isValid = False
    elif len(userData['password']) < 7:
      flash('Password must be at least 7 characters', 'register')
      isValid = False
    return isValid
  
  @staticmethod
  def validateUserData(userData):
    isValid = True

    if len(userData['username']) < 2:
      flash('Username must be greater than 2 characters', 'register')
      isValid = False
    
    if len(userData['fName']) < 2:
      flash('First Name must be at least 2 characters.', 'register')
      isValid = False

    if len(userData['lName']) < 2:
      flash('Last name must be at least than 2 characters.', 'register')
      isValid = False

    if not EMAIL_REGEX.match(userData['email']):
      flash('Invalid email format', 'register')
      isValid = False

    return isValid
  
  @staticmethod
  def verify_password(hashedPassword, plainPassword):
    return bcrypt.checkpw(plainPassword.encode('utf-8'), hashedPassword.encode('utf-8'))