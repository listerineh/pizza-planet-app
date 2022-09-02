from app.common.http_methods import GET, POST
from flask import Blueprint, request

from ..controllers import OrderController
from .base import run_service

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    return run_service(OrderController, method=POST, request=request.json)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return run_service(OrderController, method=GET, id=_id)


@order.route('/', methods=GET)
def get_orders():
    return run_service(OrderController, method=GET)
