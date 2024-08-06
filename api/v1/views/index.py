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
    return jsonify({"status": "OK"})
