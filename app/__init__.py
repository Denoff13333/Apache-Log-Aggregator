from flask import Flask
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.settings.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()
