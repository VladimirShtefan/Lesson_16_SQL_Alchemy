import enum

from sqlalchemy import text
from sqlalchemy.orm import relationship

from data_base.creat_db import db


class Role(enum.Enum):
    customer = 1
    executor = 2


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.SmallInteger)
    email = db.Column(db.String(50), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)
    phone = db.Column(db.String(10), nullable=False)

    orders = relationship('Order')
    offers = relationship('Offer')


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    star_date = db.Column(db.DateTime, server_default=text('NOW()'))
    end_date = db.Column(db.DateTime, server_default=text('NOW()'))
    address = db.Column(db.String(250), nullable=False)
    price = db.Column(db.DECIMAL, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('offer.id'))

    user = relationship('User')
    offer = relationship('Offer')


class Offer(db.Model):
    __tablename__ = 'offer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    order = relationship('Order')
    user = relationship('User')
