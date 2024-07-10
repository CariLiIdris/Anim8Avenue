from flask import Flask, jsonify, request # type: ignore
from flask_cors import CORS # type: ignore
from config import app
from controllers import shows_controller, users_controller, groups_controller, showPosts_controller, groupPosts_controller, messages_controller

CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

if __name__ == '__main__':
  app.run(debug=True, host="localhost", port=8000)