from datetime import datetime
from flask import url_for, abort, request, current_app, make_response, jsonify, g
from .. import db, auth
from ..models import Todo, User
from . import api


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username=username_or_token).filter_by()
        if not user or not user.verify_password(password):
            return False
        g.user = user
        return True


@api.route('/todos', methods=['GET'])
@auth.login_required
def get_todos():
    """ get the todos"""
    todos = Todo.query.all()

    return jsonify({'todos': [todo.to_json() for todo in todos]}), 200


@api.route('/todo/<int:todo_id>', methods=['GET'])
@auth.login_required
def get_todo(todo_id):
    """ get given todo"""
    todo = Todo.query.get_or_404(todo_id)
    if not todo:
        abort(404)
    return jsonify({'todo': todo.to_json()}), 200


@api.route('/todo/create', methods=['POST'])
@auth.login_required
def create_todo():
    if not request.json:
        abort(400)
    todo = Todo.from_json(request.json)
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_json()), 201


@api.route('/todo/delete/<int:todo_id>', methods=['DELETE'])
@auth.login_required
def delete_todo(todo_id):
    if not request.method == 'DELETE':
        abort(400)
    todo = Todo.query.get_or_404(todo_id)
    if todo is None:
        abort(404)
    if not g.user.id == todo.author_id:
        abort(403)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'result': 'Todo deleted.'}), 201


@api.route('/todo/put/<int:todo_id>', methods=['PUT'])
@auth.login_required
def put_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if todo is None:
        abort(404)
    if not g.user.id == todo.author_id:
        abort(403)
    todo.put_from_json(request.json)
    db.session.commit()
    return jsonify({'result': 'Put done.'}), 201
