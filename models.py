from flask_sqlalchemy import db

class User(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'