from flask import Flask
from flask_cors import CORS
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, resources={r"/*": {"origins": app.config["CORS_ORIGIN"]}})

    from app.routes import api

    app.register_blueprint(api.bp)

    return app
