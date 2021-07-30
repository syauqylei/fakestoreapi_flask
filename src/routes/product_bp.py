from flask import Blueprint

from src.controllers.ProductControllers import get_all

product_bp = Blueprint('product_bp', __name__)

product_bp.route('', methods=['GET'])(get_all)
