#Flask App Creation for Website
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # add Blueprints
    from .templates import index
    app.register_blueprint(index.mainbp)

    return app
