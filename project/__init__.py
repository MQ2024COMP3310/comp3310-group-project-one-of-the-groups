# Inspired by COMP3310 Wk10 Task


from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
from pathlib import Path

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

db_users = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-do-not-reveal'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db' # DATABASE_URI as main db
    CWD = Path(os.path.dirname(__file__))
    app.config['UPLOAD_DIR'] = CWD / "uploads"


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from .user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



    db.init_app(app)

    # Init users db:

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
