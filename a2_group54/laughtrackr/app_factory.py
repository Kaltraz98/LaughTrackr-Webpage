#Flask App Creation for Website
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .index import mainbp
    app.register_blueprint(mainbp)

    from .BookingHistory import bookingbp
    app.register_blueprint(bookingbp)

    from .ComedyEvents import eventsbp
    app.register_blueprint(eventsbp)

    from .login import loginbp
    app.register_blueprint(loginbp)

    from .auth import authbp
    app.register_blueprint(authbp)

    return app