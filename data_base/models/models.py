import enum

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
    age = db.Column(db.SmallInteger, db.CheckConstraint("age > 0"))
    email = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(10), nullable=False)

    # orders = relationship('Order')
    # offers = relationship('Offer')

    def convert_in_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String(250), nullable=False)
    price = db.Column(db.DECIMAL, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer)

    user = relationship('User')

    def convert_in_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }


class Offer(db.Model):
    __tablename__ = 'offer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    order = relationship('Order')
    user = relationship('User')

    def convert_in_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }
