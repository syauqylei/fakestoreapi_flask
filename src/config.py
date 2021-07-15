import os


class Development(object):
    """
    DEVELOPMENT CONFIG
    """

    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')


class Production(object):
    """
    PRODUCTION CONFIG
    """

    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')


app_config = {'development': Development, 'production': Production}
