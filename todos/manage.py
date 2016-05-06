#!/usr/bin/env/python
# coding:utf-8

import os
from app import create_app, db
from app.models import Todo, User
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Todo=Todo, User=User)

manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def createall():
    """creates the table """
    db.create_all()


@manager.command
def dropall():
    """drop the table"""
    db.drop_all()

if __name__ == '__main__':
    manager.run()
