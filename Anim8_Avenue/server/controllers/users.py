from flask import Flask, jsonify, request, session, redirect, url_for # type: ignore
from flask_cors import CORS # type: ignore
from models.user import User
from config import app

CORS(app)

@app.route('/api/users', methods=['GET'])
def getAllUsers():
  users = User.getAllUsers()
  return jsonify([user.__dict__ for user in users]) # Convert User objects to dictionaries

@app.route('/api/users/<int:userID>', methods=['GET'])
def getUserByID(userID):
  user = User.getUserByID(userID)
  if user:
    return jsonify(user.__dict__)
  else:
    return jsonify({'errorMsg': 'User not found'}), 404
  
@app.route('/api/users', methods=['POST'])
def createUser():
  data = request.get_json()
  if User.validateNewUser(data):
    userID = User.createUser(data)
    return jsonify({'message': 'User created', 'userID': userID}), 200
  else:
    return jsonify({'errorMsg': 'Validation failed'}), 400
  
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
    return jsonify({'message': 'Logout successful'}), 200