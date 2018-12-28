from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fruit(db.Model):
    __tablename__ = "fruits"
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))
    price = db.Column(db.Float)