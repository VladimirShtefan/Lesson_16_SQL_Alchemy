from flask import Blueprint, jsonify

from app.blueprints.dao.dao_utils import get_data_for_table, create_table
from app.configs.path import USER_JSON_DIR, ORDERS_JSON_DIR, OFFERS_JSON_DIR
from data_base.models.models import User, Order, Offer

orders_blueprint = Blueprint('orders_blueprint', __name__)


@orders_blueprint.before_app_first_request
def first_request():
    users_data = get_data_for_table(USER_JSON_DIR)
    create_table(users_data, User)

    orders_data = get_data_for_table(ORDERS_JSON_DIR)
    create_table(orders_data, Order)

    offers_data = get_data_for_table(OFFERS_JSON_DIR)
    create_table(offers_data, Offer)


@orders_blueprint.get('/')
def main_page():
    return 'Ok'


@orders_blueprint.get('/users/<int:uid>')
@orders_blueprint.get('/users/')
def users_page(uid=None):
    if uid is None:
        users = [user.convert_in_dict() for user in User.query.all()]
        return jsonify(users)
    else:
        user = User.query.filter(User.id == uid).first()
        return jsonify(user.convert_in_dict())


@orders_blueprint.get('/orders/<int:uid>')
@orders_blueprint.get('/orders/')
def orders_page(uid=None):
    if uid is None:
        orders = [order.convert_in_dict() for order in Order.query.all()]
        return jsonify(orders)
    else:
        order = Order.query.filter(Order.id == uid).first()
        return jsonify(order.convert_in_dict())


@orders_blueprint.get('/offers/<int:uid>')
@orders_blueprint.get('/offers/')
def offers_page(uid=None):
    if uid is None:
        offers = [offer.convert_in_dict() for offer in Offer.query.all()]
        return jsonify(offers)
    else:
        offer = Offer.query.filter(Offer.id == uid).first()
        return jsonify(offer.convert_in_dict())

