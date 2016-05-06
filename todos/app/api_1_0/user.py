from ..models import User
from . import api
from .. import db
from flask import request, jsonify


@api.route('/users', methods=['POST'])
def new_user():
    if request.headers.get('Content-Type') == 'application/json':
        try:
            username = request.json.get('username')
            password = request.json.get('password')
        except Exception, e:
            return jsonify({'error': 'bad request'}), 400
    else:
        json_response = request.get_json(True)
        username = json_response.get('username')
        password = json_response.get('password')
    if username is None or password is None:
        return jsonify({'error': 'missing arguments'}), 400
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': 'existing user'}), 400
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201
