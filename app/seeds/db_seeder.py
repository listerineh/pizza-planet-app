from flask_seeder import Seeder, Faker, generator

from app.repositories.models import Size, Ingredient, Beverage, Order
from app.seeds.utils.custom_generators import ListGenerator, PriceGenerator


sizes_len = 5
ingredients_len = 10
beverages_len = 5

size_names = ["small", "personal", "medium", "big", "familiar"]
size_prices = [5.99, 9.99, 13.99, 19.99, 24.99]
ingredients = ["pepperoni", "cheese", "salami", "tomato",
               "chicken", "meat", "mushrooms", "basil", "sardine", "cauliflower"]
beverages = ["pepsi", "fanta", "seven up", "dr pepper", "gallito"]


class SizeSeeder(Seeder):

    def run(self):
        def create_faker():
            return Faker(
                cls=Size,
                init={
                    '_id': generator.Sequence(),
                    'name': ListGenerator(size_names),
                    'price': ListGenerator(size_prices),
                }
            )

        for size in create_faker().create(sizes_len):
            self.db.session.add(size)


class IngredientSeeder(Seeder):

    def run(self):
        def create_faker():
            return Faker(
                cls=Ingredient,
                init={
                    '_id': generator.Sequence(),
                    'name': ListGenerator(ingredients),
                    'price': PriceGenerator(),
                }
            )

        for ingredient in create_faker().create(ingredients_len):
            self.db.session.add(ingredient)


class BeverageSeeder(Seeder):

    def run(self):
        def create_faker():
            return Faker(
                cls=Beverage,
                init={
                    '_id': generator.Sequence(),
                    'name': ListGenerator(beverages),
                    'price': PriceGenerator(),
                }
            )

        for beverage in create_faker().create(beverages_len):
            self.db.session.add(beverage)
