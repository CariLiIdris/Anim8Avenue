from flask import Flask, jsonify, request, session, redirect, url_for # type: ignore
from flask_cors import CORS # type: ignore
from models.user import User
from config import app

CORS(app)

# C
@app.route('/api/users', methods=['POST'])
def createUser():
  data = request.get_json()
  if User.validateNewUser(data):
    userID = User.createUser(data)
    return jsonify({'message': 'User created', 'userID': userID}), 200
  else:
    return jsonify({'errorMsg': 'Validation failed'}), 400

# R
@app.route('/api/users', methods=['GET'])
def getAllUsers():
  users = User.getAllUsers()
  # Convert User objects to dictionaries
  return jsonify([user.to_dict() for user in users]), 200 

@app.route('/api/users/<int:userID>', methods=['GET'])
def getUserByID(userID):
  user = User.getUserByID(userID)
  if user:
    return jsonify(user.to_dict()), 200
  else:
    return jsonify({'errorMsg': 'User not found'}), 404
  
@app.route('/api/users/<string:username>', methods=['GET'])
def getUserByUsername(username):
  user = User.getUserByUsername(username)
  if user:
    return jsonify(user.to_dict()), 200
  else:
    return jsonify({'errorMsg': 'User not found'}), 404

# U
@app.route('/api/user/<int:userID>', methods=['PUT'])
def updateUserByID(userID):
    data = request.get_json()
    if User.validateUserData(data):
        User.updateUserByID(userID, data)
        return jsonify({'message': 'User updated'}), 200
    else:
        return jsonify({'errorMsg': 'Validation failed'}), 400

# D
@app.route('/api/user/<int:userID>', methods=['DELETE'])
def deleteUserByID(userID):
    User.deleteUserByID(userID)
    return jsonify({'message': 'User deleted'}), 200

# Login and logout
@app.route('/api/user/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.getUserByUsername(data['username'])
    if user and User.verify_password(user.password, data['password']):
        session['userID'] = user._id
        return jsonify({'message': 'Login successful', 'user': user.to_dict()}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/user/logout', methods=['POST'])
def logout():
    session.pop('userID', None)
    session.clear()
    return jsonify({'message': 'Logout successful'}), 200