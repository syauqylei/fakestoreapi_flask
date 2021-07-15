from flask import Flask
from flask_migrate import Migrate
from .config import app_config
from .models import db
from .models.ProductModel import *
from .models.CategoryModel import *

migrate = Migrate()


def create_app(env_name):
    """
    create_app
    """
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    db.init_app(app)
    migrate = Migrate(app, db)

    import os
    print(os.getenv('DATABASE_URI'))

    @app.route('/', methods=['GET'])
    def index():
        return "Hello World"

    return app
