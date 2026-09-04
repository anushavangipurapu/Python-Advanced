from flask import Flask

from .config import Config
from .models import db
from .routes import employee_bp
from .logging_config import setup_logging


def create_app():
    app = Flask(__name__)

    setup_logging()

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(employee_bp)

    with app.app_context():
        db.create_all()

    return app