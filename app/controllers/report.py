from sqlalchemy.exc import SQLAlchemyError

from ..repositories.managers import ReportManager
from app.common.singleton import SingletonMeta


class ReportController(metaclass=SingletonMeta):
    manager = ReportManager

    @classmethod
    def get_report(cls):
        try:
            return cls.manager.get_report(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_most_requested_ingredient(cls):
        try:
            return cls.manager.get_most_requested_ingredient(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_more_revenue_month(cls):
        try:
            return cls.manager.get_more_revenue_month(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_best_customers(cls):
        try:
            return cls.manager.get_best_customers(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
