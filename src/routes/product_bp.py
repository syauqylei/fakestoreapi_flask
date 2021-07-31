from flask import Blueprint

from src.controllers.ProductControllers import get_all, get_one, get_category

product_bp = Blueprint('product_bp', __name__)

product_bp.route('', methods=['GET'])(get_all)
product_bp.route('/<int:product_id>', methods=['GET'])(get_one)

category_bp = Blueprint('category_bp', __name__)

category_bp.route('', methods=['GET'])(get_category)
