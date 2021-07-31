from flask import Flask
from flask_migrate import Migrate
from .config import app_config
from .models import db
from .routes.user_bp import user_bp
from .routes.product_bp import product_bp, category_bp

migrate = Migrate()


def create_app(env_name):
    """
    create_app
    """
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(category_bp, url_prefix='/api/category')

    @app.route('/', methods=['GET'])
    def index():
        return "Hello World"

    return app
