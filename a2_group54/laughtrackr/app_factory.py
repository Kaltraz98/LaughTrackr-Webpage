# Flask import
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    from .index import mainbp
    app.register_blueprint(mainbp)

    from .BookingHistory import bookingbp
    app.register_blueprint(bookingbp)

    from .ComedyEvents import eventsbp
    app.register_blueprint(eventsbp)

    from .auth import authbp
    app.register_blueprint(authbp)

    from . import auth
    app.register_blueprint(auth.authbp)

    return app