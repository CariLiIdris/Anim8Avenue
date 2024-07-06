from flask import Flask, jsonify, request, session, redirect, url_for # type: ignore
from flask_cors import CORS # type: ignore
from models.showPost import ShowPost
from config import app

CORS(app)

# C
@app.route('/api/posts', methods=['POST'])
def createPost():
  data = request.get_json()
  postID = ShowPost.createPost(data)
  return jsonify({'message': 'Post Created', 'postID': postID})

# R


# U


# D