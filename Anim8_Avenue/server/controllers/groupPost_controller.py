from flask import Flask, jsonify, request, session, redirect, url_for # type: ignore
from flask_cors import CORS # type: ignore
from models.groupPost import GroupPost
from config import app

CORS(app)

# C
@app.route('/api/group-posts', methods=['POST'])
def createGroupPost():
  if 'userID' not in session:
    return jsonify({'error': 'Unauthorized'}), 401

  data = request.get_json()
  data['author_id'] = session['userID']

  post_id = GroupPost.createGroupPost(data)
  return jsonify({'message': 'Post created', 'post_id': post_id}), 201

# R
@app.route('/api/group-posts',  methods=['GET'])
def getAllGroupPosts():
  groupPosts = GroupPost.getAllGroupPosts()
  return jsonify([groupPost.to_dict() for groupPost in groupPosts])

@app.route('/api/group-post/<int:postID>',  methods=['GET'])
def getGroupPostByID(postID):
  groupPost = GroupPost.getGroupPostByID(postID)
  if groupPost:
    return jsonify(groupPost.to_dict()), 200
  else:
    return jsonify({'errorMsg': 'Post not found'}), 404 

# U
@app.route('/api/group-post/<int:postID>', methods=['PUT'])
def updateGroupPostByID(postID):
  data = request.get_json()
  GroupPost.updateGroupPostByID(postID, data)
  return jsonify({'message': 'Post updated'}), 200

# D
@app.route('/api/group-post/<int:postID>', methods=['DELETE'])
def deleteGroupPostByID(postID):
    GroupPost.deleteGroupPostByID(postID)
    return jsonify({'message': 'Post deleted'}), 200