from flask import Flask, jsonify, request, session, redirect, url_for # type: ignore
from flask_cors import CORS # type: ignore
from models.show import Show
from config import app

CORS(app)

# C
@app.route('/api/shows', methods=['POST'])
def createShow():
  data = request.get_json()
  showID = Show.createShow(data)
  return jsonify({'message': 'Show created', 'showID': showID}), 200

# R
@app.route('/api/shows', methods=['GET'])
def getAllShows():
  shows = Show.getAllShows()
  return jsonify([show.__dict__ for show in shows])

@app.route('/api/shows/<int:showID>', methods=['GET'])
def getShowByID(showID):
  show = Show.getShowByID(showID)
  if show:
    return jsonify(show.__dict__)
  else:
    return jsonify({'errorMsg': 'Show not found'}), 404

# U
@app.route('/api/show/<int:showID>', methods=['PUT'])
def updateShowByID(showID):
  data = request.get_json()
  Show.updateShowByID(showID, data)
  return jsonify({'message': 'Show updated'}), 200

# D
@app.route('/api/show/<int:showID>', methods=['DELETE'])
def deleteShowByID(showID):
    Show.deleteShowByID(showID)
    return jsonify({'message': 'Show deleted'}), 200