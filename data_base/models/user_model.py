from data_base.create_db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
