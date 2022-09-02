from datetime import datetime
from collections import Counter

from sqlalchemy.exc import SQLAlchemyError

from app.plugins import db
from ..models import Order, IngredientsDetail, Ingredient


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
