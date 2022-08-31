from msilib import sequence
from flask_seeder import Faker, generator

from app.repositories.models import Size, Ingredient, Beverage, Order, IngredientsDetail, BeveragesDetail
from app.seeds.utils.custom_generators import ListGenerator, PriceGenerator
from app.seeds.data.lists import *
from app.seeds.data.sizes import *


def create_size_faker():
    return Faker(
        cls=Size,
        init={
            '_id': generator.Sequence(),
            'name': ListGenerator(size_names),
            'price': ListGenerator(size_prices),
        }
    )


def create_ingredient_faker():
    return Faker(
        cls=Ingredient,
        init={
            '_id': generator.Sequence(),
            'name': ListGenerator(ingredients),
            'price': PriceGenerator(),
        }
    )


def create_beverage_faker():
    return Faker(
        cls=Beverage,
        init={
            '_id': generator.Sequence(),
            'name': ListGenerator(beverages),
            'price': PriceGenerator(),
        }
    )


def create_order_faker(order: dict):
    return Faker(
        cls=Order,
        init={
            '_id': order['_id'],
            'client_name': order['client_name'],
            'client_dni': order['client_dni'],
            'client_address': order['client_address'],
            'client_phone': order['client_phone'],
            'date': order['date'],
            'total_price': order['total_price'],
            'size_id': order['size_id'],
        }
    )


def create_ingredients_detail_faker(data: dict):
    return Faker(
        cls=IngredientsDetail,
        init={
            '_id': data['id'],
            'ingredient_price': data['ingredient_price'],
            'order_id': data['order_id'],
            'ingredient_id': data['ingredient_id'],
        }
    )


def create_beverages_detail_faker(data: dict):
    return Faker(
        cls=BeveragesDetail,
        init={
            '_id': data['id'],
            'beverage_price': data['beverage_price'],
            'order_id': data['order_id'],
            'beverage_id': data['beverage_id'],
        }
    )
