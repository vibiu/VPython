import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'vibiu_s_secret_key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # for windows
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'data.sqlite')

    # for Unix
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'data.sqlite')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + \
        os.path.join(basedir, 'data.sqlite')

QLALCHEMY_DATABASE_URI = os.environ.get(
    'TEST_DATABASE_URI') or 'mysql://pythonamdin:123456@localhost/pythonDB'

config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,

    'default': DevelopmentConfig
}
