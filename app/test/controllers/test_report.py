import pytest
from app.controllers import ReportController


def test_get_report(app, create_orders):
    report, error = ReportController.get_report()
    pytest.assume(error is None)
    pytest.assume(report['best_customers'])
    pytest.assume(report['more_revenue_month'])
    pytest.assume(report['most_requested_ingredient'])


def test_get_most_requested_ingredient(app, create_orders):
    most_requested_ingredient, error = ReportController.get_most_requested_ingredient()
    pytest.assume(error is None)
    pytest.assume(most_requested_ingredient['name'])
    pytest.assume(most_requested_ingredient['count'])


def test_get_more_revenue_month(app, create_orders):
    more_revenue_month, error = ReportController.get_more_revenue_month()
    pytest.assume(error is None)
    pytest.assume(more_revenue_month['month'])


def test_get_best_customers(app, create_orders):
    best_customers, error = ReportController.get_best_customers()
    pytest.assume(error is None)
    pytest.assume(best_customers['customers'])
    pytest.assume(len(best_customers['customers']) == 3)
