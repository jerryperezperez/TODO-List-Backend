from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
