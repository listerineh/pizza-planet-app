from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import IngredientController
from .base import run_service

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    return run_service(IngredientController, method=POST, request=request.json)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return run_service(IngredientController, method=PUT, request=request.json)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return run_service(IngredientController, method=GET, id=_id)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return run_service(IngredientController, method=GET)
