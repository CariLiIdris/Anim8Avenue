from flask import Flask, jsonify, request, session, redirect, url_for # type: ignore
from flask_cors import CORS # type: ignore
from models.showPost import ShowPost
from config import app

CORS(app)

# C
@app.route('/api/show-posts', methods=['POST'])
def createShowPost():
  if 'userID' not in session:
    return jsonify({'error': 'Unauthorized'}), 401

  data = request.get_json()
  data['author_id'] = session['userID']

  post_id = ShowPost.createShowPost(data)
  return jsonify({'message': 'Post created', 'post_id': post_id}), 201

# R
@app.route('/api/show-posts',  methods=['GET'])
def getAllShowPosts():
  showPosts = ShowPost.getAllShowPosts()
  return jsonify([showPost.to_dict() for showPost in showPosts])

@app.route('/api/show-post/<int:postID>',  methods=['GET'])
def getShowPostByID(postID):
  showPost = ShowPost.getShowPostByID(postID)
  if showPost:
    return jsonify(showPost.to_dict()), 200
  else:
    return jsonify({'errorMsg': 'Post not found'}), 404 

# U
@app.route('/api/show-post/<int:postID>', methods=['PUT'])
def updateShowPostByID(postID):
  data = request.get_json()
  ShowPost.updateShowPostByID(postID, data)
  return jsonify({'message': 'Post updated'}), 200

# D
@app.route('/api/show-post/<int:postID>', methods=['DELETE'])
def deleteShowPostByID(postID):
    ShowPost.deleteShowPostByID(postID)
    return jsonify({'message': 'Post deleted'}), 200