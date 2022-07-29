from flask import Blueprint

from app.blueprints.dao.dao_utils import get_data_for_table, create_table
from app.configs.path import USER_JSON_DIR, ORDERS_JSON_DIR, OFFERS_JSON_DIR
from data_base.models.user_model import User, Order, Offer

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
    return ''
