# Imports
import os
from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, current_user

# SQL extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'devkey')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comedydb.sqlite'

    # extensions
    Bootstrap5(app)
    db.init_app(app)

    # Login manager 
    login_manager = LoginManager()
    login_manager.login_view = 'auth.logged_in'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    # blueprints
    from .index import mainbp
    from .ComedyEvents import eventsbp
    from .auth import authbp
    from .BookingHistory import bookingbp

    app.register_blueprint(mainbp)
    app.register_blueprint(eventsbp)
    app.register_blueprint(authbp)
    app.register_blueprint(bookingbp)

    return app