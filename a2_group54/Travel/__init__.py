#Flask App Creation for Website
from flask import Flask
def create_app():
    print(__name__)  
    app = Flask(__name__)  
    
    # Register Blueprint from Views
    from . import views
    app.register_blueprint(views.mainbp)
    app.secret_key = 'asecret'
   
    return app

