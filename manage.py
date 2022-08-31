

import pytest
import subprocess
from flask.cli import FlaskGroup
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import Ingredient, Order, IngredientsDetail, BeveragesDetail, Size, Beverage


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)

seeder = FlaskSeeder()
seeder.init_app(flask_app, db)


@manager.command('drop_db', with_appcontext=False)
def drop_db():
    subprocess.run('python ./manage.py db downgrade base')
    subprocess.run('python ./manage.py db upgrade')
    print('Database dropped succesfully!')


@manager.command('fill_db', with_appcontext=False)
def fill_db():
    subprocess.run('python ./manage.py seed run --root app/seeds')
    print('Database filled succesfully!')


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', './app/test'])


if __name__ == '__main__':
    manager()
