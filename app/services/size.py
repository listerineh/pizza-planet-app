from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import SizeController
from .base import run_service

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
def create_size():
    return run_service(SizeController, method=POST, request=request.json)


@size.route('/', methods=PUT)
def update_size():
    return run_service(SizeController, method=PUT, request=request.json)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return run_service(SizeController, method=GET, id=_id)


@size.route('/', methods=GET)
def get_sizes():
    return run_service(SizeController, method=GET)
