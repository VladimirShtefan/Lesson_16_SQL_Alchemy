import enum

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
    role = db.Column(db.Enum(Role), nullable=False)
    phone = db.Column(db.String(10), nullable=False)

    customers = db.relationship('Order', foreign_keys='Order.customer_id', cascade='all, delete')
    executors = db.relationship('Order', foreign_keys='Order.executor_id', cascade='all, delete')

    offers = db.relationship('Offer', foreign_keys='Offer.executor_id', cascade='all, delete')

    def convert_in_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role.name,
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
    price = db.Column(db.Integer, db.CheckConstraint('price > 0'))
    # один user ко может создавать много заказов
    customer_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))
    # один user может брать на выполнение много заказов
    executor_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))

    # связь двунаправленная
    customer_constraint: User = db.relationship('User', foreign_keys=[customer_id])
    executor_constraint: User = db.relationship('User', foreign_keys=[executor_id])

    orders = db.relationship('Offer', cascade='all, delete')

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
            "executor_id": self.executor_id,
            'customer_info': self.customer_constraint.convert_in_dict(),
            'executor_info': self.executor_constraint.convert_in_dict()
        }


class Offer(db.Model):
    __tablename__ = 'offer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey(f'{Order.__tablename__}.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))

    orders_constraint: Order = db.relationship('Order', foreign_keys=[order_id])
    executor_constraint: User = db.relationship('User', foreign_keys=[executor_id])

    def convert_in_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
            'order_info': self.orders_constraint.convert_in_dict(),
            'executor_info': self.executor_constraint.convert_in_dict()
        }
