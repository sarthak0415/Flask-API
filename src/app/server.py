from __future__ import absolute_import, division, with_statement
import logging
import os
from flask import Flask
from src.config.setting import settings
from src.api.index import api
from src.db.database import db

# Flask App Initialization
app = Flask(__name__)

def connect_to_db(app, db_uri):
    """Connect the database to Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def connect_to_api(app):
    # Flask API Initialization
    api.init_app(app)


def connect_logger(app):
    console = logging.getLogger('console')


def connect(app):
    '''
    Function to connect Flask app
    '''

    # Fetch Settings
    app.config.from_object(settings[os.environ.get('APPLICATION_ENV', 'default')])

    # Logs Initialization
    console = logging.getLogger('console')

    # Database ORM Initialization
    connect_to_db(app, "postgresql://nexfac:123456@localhost:54321/core")

    # Flask API Initialization
    connect_to_api(app)

# Run the connect function to init app
connect(app)
