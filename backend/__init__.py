from flask import Flask
from datetime import datetime, timedelta, timezone
from flask_sqlalchemy import SQLAlchemy
from .api import api as api_blueprint
from .auth import auth as auth_blueprint
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-type'
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['JWT_SECRET_KEY'] = 'Whereof one cannot speak, thereof one must remain silent'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    
    db.init_app(app)
    jwt = JWTManager(app)

    # blueprint for auth routes in our app
    app.register_blueprint(auth_blueprint)

    # blueprint for API
    app.register_blueprint(api_blueprint)

    return app

