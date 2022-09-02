from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import BeverageController
from .base import run_service

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_beverage():
    return run_service(BeverageController, method=POST, request=request.json)


@beverage.route('/', methods=PUT)
def update_beverage():
    return run_service(BeverageController, method=PUT, request=request.json)


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return run_service(BeverageController, method=GET, id=_id)


@beverage.route('/', methods=GET)
def get_beverages():
    return run_service(BeverageController, method=GET)
