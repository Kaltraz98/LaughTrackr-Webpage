from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # for displaying forms quickly
    Bootstrap5(app)

    # secret key for the session object
    app.secret_key = 'somerandomvalue'

    # Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comedydb.sqlite'
    db.init_app(app)
    
    # add Blueprints
    from . import index
    app.register_blueprint(index.mainbp)
    from . import ComedyEvents
    app.register_blueprint(ComedyEvents.eventsbp)
    from . import auth
    app.register_blueprint(auth.authbp)

    return app