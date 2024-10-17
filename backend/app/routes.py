from flask import send_from_directory
from app import app

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

""" @app.route('/')
def home():
    return "Hello, Flask!" """