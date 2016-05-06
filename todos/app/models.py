from datetime import datetime
from . import db
from werkzeug import generate_password_hash, check_password_hash
from flask import current_app, g
from flask.ext.login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature


column = db.Column


class Todo(db.Model):
    __tablename__ = 'todos'
    id = column('id', db.Integer, primary_key=True)
    title = column(db.String(64))
    body = column(db.String(1024))
    done = column(db.Boolean)
    timestamp = column(db.DateTime)
    author_id = column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.done = False
        self.timestamp = datetime.utcnow()
        self.author_id = g.user.id

    @staticmethod
    def from_json(json_post):
        title = json_post.get('title')
        body = json_post.get('body')
        if body is None or body == '':
            raise ValidationError('post does not have a body')
        return Todo(title, body)

    def put_from_json(self, json_post):
        if json_post.get('title'):
            self.title = json_post.get('title')
        if json_post.get('body'):
            self.body = json_post.get('body')
        self.timestamp = datetime.utcnow()

    def to_json(self):
        todo_json = {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'done': self.done,
            'author': User.query.filter_by(id=self.author_id).first().username
        }
        return todo_json

    def __repr__(self):
        return "<Todo %r>" % self.title


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = column(db.Integer, primary_key=True)
    username = column(db.String(64), unique=True, index=True)
    password_hash = column(db.String(128))
    todos = db.relationship('Todo', backref='author', lazy='dynamic')

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.confi['SECRET_KEY'])
        try:
            data = s.loads(token)
            except SignatureExpired:
                return None
            except BadSignature:
                return None
        user = User.query.get(data['id'])
        return user

    def __repr_(self):
        return "<User %r>" % self.username
