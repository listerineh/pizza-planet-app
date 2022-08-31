from flask_seeder import Seeder
from random import randint

from app.seeds.utils.functions import get_orders_order, get_random_dates
from app.seeds.fakers import *
from app.seeds.data.sizes import *
from app.seeds.data.lists import client_names
from app.test.utils.functions import get_random_phone


class DBSeeder(Seeder):

    def save(self, data: list, name: str):
        for item in data:
            self.db.session.add(item)
        print(
            f'{len(data)} {name} succesfully added to the database!')

    def run(self):

        # Creating data

        sizes = create_size_faker().create(sizes_len)
        ingredients = create_ingredient_faker().create(ingredients_len)
        beverages = create_beverage_faker().create(beverages_len)

        # Creating orders

        orders_order = get_orders_order(users_len, orders_len)
        counter = 1
        index = 0

        dates = get_random_dates(orders_len)
        orders = []

        for order in orders_order:
            new_order = {
                '_id': counter,
                'client_name': client_names[index],
                'client_dni': client_names[index],
                'client_address': client_names[index],
                'client_phone': get_random_phone(),
                'date': dates[counter-1],
                'total_price': 0,
                'size_id': randint(1, sizes_len),
            }

            for _ in range(order):
                orders.append(create_order_faker(new_order).create()[0])
                counter += 1

            index += 1

        # Savind the data

        self.save(sizes, 'sizes')
        self.save(ingredients, 'ingredients')
        self.save(beverages, 'beverages')
        self.save(orders, 'orders')
