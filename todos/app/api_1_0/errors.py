from flask import request, jsonify
from . import api


@api.app_errorhandler(404)
def page_not_found(error):
    response = jsonify({'errror': 'not found'})
    response.status_code = 404
    return response


@api.app_errorhandler(400)
def bad_request(error):
    response = jsonify({'error': 'bad request'})
    response.status_code = 400
    return response


@api.app_errorhandler(403)
def Forbidden(error):
    response = jsonify({'error': 'forbidden'})
    response.status_code = 403
    return response
