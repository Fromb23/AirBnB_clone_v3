#!/usr/bin/python3
"""Flask application setup."""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def storage_close(exception):
    """Close storage on app teardown."""
    storage.close()


@app.errorhandler(404)
def error404(error):
    """"Return error 404"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
