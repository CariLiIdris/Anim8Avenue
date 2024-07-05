from config.mysqlconnection import connectToMySQL
from flask import flash # type: ignore
import re
import bcrypt # type: ignore

# Email format regex
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# User class
class User:
  DB = 'anim8AveSchema'
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
    self.messages = []
    self.groups = []
    self.shows = []

  def to_dict(self):
        return {
            '_id': self._id,
            'username': self.username,
            'fName': self.fName,
            'lName': self.lName,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'friends': self.friends,
            'messages': self.messages,
            'groups': self.groups,
            'shows': self.shows
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
      return cls(result[0])
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
  def getAllUsers(cls):
    query = '''
              SELECT * FROM users;
            '''
    results = connectToMySQL(cls.DB).query_db(query)
    users = []

    for user in results:
      users.append( cls(user) )
    return users
  
  @classmethod
  def updateUserByID(cls, userID, data):
    query = '''
              UPDATE users
              SET username=%(username)s, fName=%(fName)s, lName=%(lName)s, email=%(email)s
              WHERE _id = %(_id)s;
            '''
    data['_id'] = userID
    return connectToMySQL(cls.DB).query_db(query, data)
  
  @classmethod
  def deleteUserByID(cls, userID):
    query = '''
              DELETE FROM users 
              WHERE _id = %(_id)s;
            '''
    data = {'_id': userID}
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

    return isValid
  
  @staticmethod
  def verify_password(hashedPassword, plainPassword):
    return bcrypt.checkpw(plainPassword.encode('utf-8'), hashedPassword.encode('utf-8'))