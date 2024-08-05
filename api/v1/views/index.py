#!/usr/bin/python3
"""
    Flask API endpoint
"""
from flask import json, Response
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/stats', methods=['GET'])

def status():
    """Return the API status"""
    counts = {
            "amenities": storage.count("Amenities"),
            "cities": storage.count("City"),
            "places": storage.count("Places"),
            "reviews": storage.count("Reviews"),
            "states": storage.count("State"),
            "users": storage.count("User")
            }
    response = Response(
        json.dumps(counts, indent=2),
        mimetype='application/json'
        )
    return response
