import os
from flask import Flask
from app.admin import setup_admin
from app.models import db

app = Flask(__name__)
# Setup the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Initializes SQLAlchemy instance with flask
db.init_app(app)
setup_admin(app)

# Creates the database
with app.app_context():
    db.create_all()

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)