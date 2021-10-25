from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now())

    # the next line helps to link a valid id from existing user into user_id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
# can add more classes here, inherit db.Model
# study many to one relationship with objects

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    # capital N to reference the name of the class
    notes = db.relationship('Note')
