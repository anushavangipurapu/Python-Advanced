from flask import Flask
from database import db
from routes import employee_bp
import logging


app = Flask(__name__)


# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Connect database with Flask
db.init_app(app)


# Logging configuration
logging.basicConfig(
    filename="employee_api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Register employee routes
app.register_blueprint(employee_bp)


# Create database tables
with app.app_context():
    db.create_all()


# Home route
@app.route("/")
def home():
    return {
        "message": "Employee REST API is running"
    }


# Start Flask application
if __name__ == "__main__":
    app.run(debug=True)