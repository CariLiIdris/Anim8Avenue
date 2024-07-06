from flask import Flask, jsonify, request, session, redirect, url_for # type: ignore
from flask_cors import CORS # type: ignore
from models.group import Group
from config import app

CORS(app)

# C
@app.route('/api/groups', methods=['POST'])
def createGroup():
  data = request.get_json()
  data['owner_id'] = session['userID']
  groupID = Group.createGroup(data)
  return jsonify({'message': 'Group created', 'groupID': groupID}), 200

# R
@app.route('/api/groups', methods=['GET'])
def getAllGroups():
  groups = Group.getAllGroups()
  return jsonify([group.to_dict() for group in groups])

@app.route('/api/groups/<int:groupID>', methods=['GET'])
def getGroupByID(groupID):
  group = Group.getGroupByID(groupID)
  if group:
    return jsonify(group.to_dict())
  else:
    return jsonify({'errorMsg': 'Group not found'}), 404

# U
@app.route('/api/group/<int:groupID>', methods=['PUT'])
def updateGroupByID(groupID):
  data = request.get_json()
  Group.updateGroupByID(groupID, data)
  return jsonify({'message': 'Group updated'}), 200

# D
@app.route('/api/group/<int:groupID>', methods=['DELETE'])
def deleteGroupByID(groupID):
    Group.deleteGroupByID(groupID)
    return jsonify({'message': 'Group deleted'}), 200