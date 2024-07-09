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
    return jsonify({'message': 'User created', 'User': data , 'userID': userID}), 200
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

# Friend controls
@app.route('/api/user/<int:userID>/friends', methods=['GET'])
def getUserFriends(userID):
    user = User.getUserByID(userID)
    if user:
        return jsonify([friend.to_dict() for friend in user.friends]), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/users/friend', methods=['POST'])
def addFriend():
    if 'userID' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = session['userID']
    friend_username = request.json.get('friend_username')
    if not friend_username:
        return jsonify({'error': 'Friend username required'}), 400

    friend_id = User.getUserIDByUsername(friend_username)
    if not friend_id:
        return jsonify({'error': 'Friend not found'}), 404

    User.addFriend(user_id, friend_id)
    return jsonify({'message': 'Friend added'}), 201

@app.route('/api/user/<int:userID>/friend', methods=['DELETE'])
def removeFriend(userID):
    if 'userID' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    friend_username = request.json.get('friend_username')
    if not friend_username:
        return jsonify({'error': 'Friend username required'}), 400

    friend_id = User.getUserIDByUsername(friend_username)
    if not friend_id:
        return jsonify({'error': 'Friend not found'}), 404

    User.removeFriend(userID, friend_id)
    return jsonify({'message': 'Friend removed'}), 200