from flask import Blueprint, jsonify, request

from app.blueprints.dao.dao_utils import get_data_for_table, create_table, DataBase
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
    return jsonify({'status': 'ok'})


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


@orders_blueprint.post('/users/')
def add_user():
    user = request.get_json()
    new_user = DataBase(User).add_object(user)
    return jsonify(new_user)


@orders_blueprint.put('/users/<int:uid>')
def update_user(uid: int):
    user = request.get_json()
    new_user = DataBase(User).update_object(user, uid)
    return jsonify(new_user)


@orders_blueprint.delete('/users/<int:uid>')
def delete_user(uid: int):
    deleted_user = DataBase(User).delete_object(uid)
    return jsonify(deleted_user)


@orders_blueprint.post('/orders/')
def add_order():
    order = request.get_json()
    new_order = DataBase(Order).add_object(order)
    return jsonify(new_order)


@orders_blueprint.put('/orders/<int:oid>')
def update_order(oid: int):
    order = request.get_json()
    new_order = DataBase(Order).update_object(order, oid)
    return jsonify(new_order)


@orders_blueprint.delete('/orders/<int:oid>')
def delete_order(oid: int):
    deleted_order = DataBase(Order).delete_object(oid)
    return jsonify(deleted_order)


@orders_blueprint.post('/offers/')
def add_offer():
    offer = request.get_json()
    new_offer = DataBase(Offer).add_object(offer)
    return jsonify(new_offer)


@orders_blueprint.put('/offers/<int:oid>')
def update_offer(oid: int):
    offer = request.get_json()
    new_offer = DataBase(Offer).update_object(offer, oid)
    return jsonify(new_offer)


@orders_blueprint.delete('/offers/<int:oid>')
def delete_offer(oid: int):
    deleted_offer = DataBase(Offer).delete_object(oid)
    return jsonify(deleted_offer)
