from datetime import datetime
from typing import Any, List, Optional, Sequence
from collections import Counter

from sqlalchemy.sql import text, column
from sqlalchemy.exc import SQLAlchemyError

from .models import Ingredient, Order, IngredientsDetail, BeveragesDetail, Size, Beverage, db
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, BeverageSerializer, ma)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all((IngredientsDetail(order_id=new_order._id, ingredient_id=ingredient._id, ingredient_price=ingredient.price)
                             for ingredient in ingredients))
        cls.session.add_all((BeveragesDetail(order_id=new_order._id, beverage_id=beverage._id, beverage_price=beverage.price)
                             for beverage in beverages))
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()


class ReportManager:
    order_model = Order
    ingredients_detail_model = IngredientsDetail
    session = db.session

    @classmethod
    def get_report(cls):
        return {
            'most_requested_ingredient': cls.get_most_requested_ingredient(),
            'more_revenue_month': cls.get_more_revenue_month(),
            'best_customers': cls.get_best_customers(),
        }

    @classmethod
    def get_most_requested_ingredient(cls):
        ingredient_details = cls.ingredients_detail_model.query.all()
        ingredient_ids = [ingredient_detail.ingredient_id
                          for ingredient_detail in ingredient_details]

        if len(ingredient_ids) > 0:
            most_requested_ingredient = {
                'id': '',
                'counter': 0,
            }

            counter = Counter(ingredient_ids)

            for key in counter:
                if counter[key] > most_requested_ingredient['counter']:
                    most_requested_ingredient['counter'] = counter[key]
                    most_requested_ingredient['id'] = key

            ingredient = Ingredient.query.get(most_requested_ingredient['id'])

            return {
                'name': ingredient.name,
                'count': most_requested_ingredient['counter'],
            }
        else:
            raise SQLAlchemyError("Any order registered in the database")

    @classmethod
    def get_more_revenue_month(cls):
        orders = cls.order_model.query.all()
        order_dates = [order.date for order in orders]

        if (len(order_dates) > 0):
            months = [date.split('/')[1] for date in order_dates]
            more_revenue_month = {
                'month': '',
                'counter': 0,
            }

            counter = Counter(months)

            for key in counter:
                if counter[key] > more_revenue_month['counter']:
                    more_revenue_month['counter'] = counter[key]
                    more_revenue_month['month'] = key

            date = datetime(
                month=int(more_revenue_month['month']), year=1, day=1)

            return {
                'month': date.strftime('%B')
            }
        else:
            raise SQLAlchemyError("Any order registered in the database")

    @classmethod
    def get_best_customers(cls):
        orders = cls.order_model.query.all()
        order_client_info = [{'dni': order.client_dni,
                              'name': order.client_name} for order in orders]

        if len(order_client_info) > 0:
            order_client_dnis = [order.client_dni for order in orders]
            counter = Counter(order_client_dnis)
            needed_customers = 3

            sorted_best_customers = sorted(
                dict(counter).items(), key=lambda x: x[1], reverse=True)

            def get_name_by_dni(dni):
                for client_info in order_client_info:
                    if client_info['dni'] == dni:
                        return client_info['name']

                return None

            return {
                'customers': [
                    {
                        'dni': sorted_best_customers[index][0],
                        'name': get_name_by_dni(sorted_best_customers[index][0]),
                        'purchases': sorted_best_customers[index][1],
                    } for index in range(needed_customers)
                ]
            }
        else:
            raise SQLAlchemyError("Any order registered in the database")
