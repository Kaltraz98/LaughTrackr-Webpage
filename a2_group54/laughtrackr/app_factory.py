#Flask App Creation for Website
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .templates import index
    app.register_blueprint(index.mainbp)
    from .templates import login
    app.register_blueprint(login.destbp)
    from .templates import BookingHistory
    app.register_blueprint(BookingHistory.destbp)
    from .templates import Events
    app.register_blueprint(Events.destbp)
    from .templates import NewEvent
    app.register_blueprint(NewEvent.destbp)

    return app