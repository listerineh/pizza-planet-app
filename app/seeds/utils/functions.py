from datetime import datetime, timedelta
from random import randrange, randint, choice


def get_orders_order(users_len: int, orders_len: int):
    """Function to randomly determine the number of orders given a number of users"""
    orders_order = []

    while True:
        for _ in range(users_len):
            orders_order.append(randint(1, orders_len//2))

        sum_orders = sum(orders_order)
        if sum_orders > orders_len:
            orders_order.clear()
        else:
            orders_order[-1] += orders_len - sum_orders
            break

    return orders_order


def get_random_dates(dates_number: int):

    start_date = datetime.strptime('1/1/2018', '%m/%d/%Y')
    end_date = datetime.strptime('1/1/2022', '%m/%d/%Y')

    random_dates = []

    for _ in range(dates_number):
        delta = end_date - start_date
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)

        random_dates.append(
            str((start_date + timedelta(seconds=random_second)).strftime("%d/%m/%Y")))

    return random_dates


def get_random_items(data: list):
    number_of_ingredients = randint(1, len(data))
    random_ingredients = []
    saved_names = []

    counter = 0

    while counter < number_of_ingredients:
        random_ingredient = choice(data)

        if not random_ingredient.name in saved_names:
            random_ingredients.append(random_ingredient)
            saved_names.append(random_ingredient.name)
            counter += 1

    return random_ingredients


def calculate_total_order_price(size_prize: float, ingredients: list, beverages: list):
    total_price = size_prize + \
        sum(ingredient.ingredient_price for ingredient in ingredients) + \
        sum(beverage.beverage_price for beverage in beverages)

    return round(total_price, 2)
