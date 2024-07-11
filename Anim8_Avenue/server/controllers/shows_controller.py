from flask import Flask, jsonify, request, session, logging, make_response # type: ignore
from flask_cors import CORS # type: ignore
from models.show import Show
from config import app
import os
from werkzeug.utils import secure_filename # type: ignore

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

def allowed_file(filename):
    return '.' in filename and \
      filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Create show
@app.route('/api/shows', methods=['POST'])
def createShow():
    data = request.form.to_dict()
    if 'image' in request.files:
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data['image_url'] = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    data['owner_id'] = session.get('userID')
    if not data['owner_id']:
        return jsonify({'error': 'User not authenticated'}), 401
    try:
        showID = Show.createShow(data)
        return jsonify({'message': 'Show created', 'showID': showID}), 200
    except Exception as e:
        app.logger.error(f"Error creating show: {e}")
        return jsonify({'error': str(e)}), 500

# Get all shows
@app.route('/api/shows', methods=['GET'])
def getAllShows():
    shows = Show.getAllShows()
    return jsonify([show.to_dict() for show in shows])

# Get show by ID
@app.route('/api/shows/<int:showID>', methods=['GET'])
def getShowByID(showID):
    show = Show.getShowByID(showID)
    if show:
        return jsonify(show.to_dict())
    else:
        return jsonify({'errorMsg': 'Show not found'}), 404

# Update show
@app.route('/api/show/<int:showID>', methods=['PUT'])
def updateShowByID(showID):
    data = request.form.to_dict()
    if 'image_url' in request.files:
        image = request.files['image_url']
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data['image_url'] = filename
    try:
        Show.updateShowByID(showID, data)
        return jsonify({'message': 'Show updated'}), 200
    except Exception as e:
        app.logger.error(f"Error updating show: {e}")
        return jsonify({'error': str(e)}), 500

# Delete show
@app.route('/api/show/<int:showID>', methods=['DELETE'])
def deleteShowByID(showID):
    Show.deleteShowByID(showID)
    return jsonify({'message': 'Show deleted'}), 200

# Get all categories
@app.route('/api/categories', methods=['GET'])
def getCategories():
    try:
        categories = Show.getAllCategories()
        return jsonify(categories), 200
    except Exception as e:
        app.logger.error(f"Error fetching categories: {e}")
        return jsonify({'error': str(e)}), 500