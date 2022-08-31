from flask_seeder import Seeder
from random import randint, choice

from app.seeds.utils.functions import get_orders_order, get_random_dates, get_random_items, calculate_total_order_price
from app.seeds.fakers import *
from app.seeds.data.sizes import *
from app.seeds.data.lists import client_names
from app.test.utils.functions import get_random_phone


class DBSeeder(Seeder):

    def save(self, data: list):
        for item in data:
            self.db.session.add(item)

    def run(self):

        # Creating data

        sizes_faker = create_size_faker().create(sizes_len)
        ingredients_faker = create_ingredient_faker().create(ingredients_len)
        beverages_faker = create_beverage_faker().create(beverages_len)

        # Creating orders

        orders_order = get_orders_order(users_len, orders_len)
        order_counter = 1
        ingredients_counter = 1
        beverages_counter = 1
        users_index = 0

        dates = get_random_dates(orders_len)
        orders = []
        ingredients_detail = []
        beverages_detail = []

        for order in orders_order:

            random_number = get_random_phone()

            for _ in range(order):

                random_size = choice(sizes_faker)

                new_order = {
                    '_id': order_counter,
                    'client_name': client_names[users_index],
                    'client_dni': client_names[users_index],
                    'client_address': client_names[users_index],
                    'client_phone': random_number,
                    'date': dates[order_counter-1],
                    'total_price': 0,
                    'size_id': random_size._id,
                }

                faker_order = create_order_faker(new_order).create()[0]
                random_ingredients = get_random_items(ingredients_faker)
                random_beverages = get_random_items(beverages_faker)

                for random_ingredient in random_ingredients:
                    new_ingredients_detail = {
                        '_id': ingredients_counter,
                        'ingredient_price': random_ingredient.price,
                        'order_id': faker_order._id,
                        'ingredient_id': random_ingredient._id,
                    }

                    ingredients_detail.append(create_ingredients_detail_faker(
                        new_ingredients_detail).create()[0])

                    ingredients_counter += 1

                for random_beverage in random_beverages:
                    new_beverages_detail = {
                        '_id': beverages_counter,
                        'beverage_price': random_beverage.price,
                        'order_id': faker_order._id,
                        'beverage_id': random_beverage._id,
                    }

                    beverages_detail.append(create_beverages_detail_faker(
                        new_beverages_detail).create()[0])

                    beverages_counter += 1

                faker_order.total_price = calculate_total_order_price(
                    random_size.price, ingredients_detail, beverages_detail)

                self.save(ingredients_detail)
                self.save(beverages_detail)

                ingredients_detail.clear()
                beverages_detail.clear()

                orders.append(faker_order)
                order_counter += 1

            users_index += 1

        # Savind the data

        self.save(sizes_faker)
        self.save(ingredients_faker)
        self.save(beverages_faker)
        self.save(orders)
