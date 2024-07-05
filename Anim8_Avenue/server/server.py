from flask import Flask, jsonify, request # type: ignore
from flask_cors import CORS # type: ignore
from controllers import users
from config import app

if __name__ == '__main__':
  app.run(debug=True, host="localhost", port=8000)