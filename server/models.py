from config import db

class Camper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    signups = db.relationship("Signup", backref="camper", cascade="all, delete")

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    difficulty = db.Column(db.Integer)
    signups = db.relationship("Signup", backref="activity", cascade="all, delete")

class Signup(db.Model):
    __tablename__ = "signups"

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)
    camper_id = db.Column(db.Integer, db.ForeignKey("camper.id"))
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"))