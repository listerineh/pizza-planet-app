import pytest

from app.test.utils.functions import get_random_string, get_random_price


def test_get_report_service__returns_status_200__with_orders(client, create_orders, report_uri):
    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))
    pytest.assume(response.json['best_customers'])
    pytest.assume(response.json['more_revenue_month'])
    pytest.assume(response.json['most_requested_ingredient'])
