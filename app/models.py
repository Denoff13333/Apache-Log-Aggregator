from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(15), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    request_method = db.Column(db.String(10), nullable=False)
    request_path = db.Column(db.String(255), nullable=False)
    status_code = db.Column(db.Integer, nullable=False)
    user_agent = db.Column(db.String(255), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
