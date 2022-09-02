from app.common.http_methods import GET
from flask import Blueprint

from ..controllers import ReportController
from .base import run_service

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    return run_service(ReportController, method='REPORT')
