from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from MyApp.config import Config
import os


db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(Config)

    with app.app_context():
        db.init_app(app)
        ma.init_app(app)
    
    from MyApp.bp_main.routes import main

    app.register_blueprint(main)


    return app