from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    Bootstrap5(app)
    app.secret_key = 'somerandomvalue'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comedydb.sqlite'
    db.init_app(app)

    from flask_login import LoginManager, current_user
    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.logged_in'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    # Blueprints
    from . import index
    app.register_blueprint(index.mainbp)
    from . import ComedyEvents
    app.register_blueprint(ComedyEvents.eventsbp)
    from . import auth
    app.register_blueprint(auth.authbp)

    return app