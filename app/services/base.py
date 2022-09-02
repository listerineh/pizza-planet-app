from flask import jsonify, Request
from typing import Optional

from app.common.http_methods import GET, POST, PUT


def run_service(EntityController, method, request: Optional[Request] = None, id: Optional[int] = None):

    entity, error = EntityController.get_by_id(id) if id else EntityController.get_all() if method == GET else EntityController.create(
        request) if method == POST else EntityController.update(request) if method == PUT else EntityController.get_report()

    response = entity if not error else {'error': error}
    status_code = 200 if entity else 404 if not error else 400
    return jsonify(response), status_code
