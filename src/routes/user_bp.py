from flask import Blueprint

from src.controllers.UserControllers import login, register

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/login', methods=['POST'])(login)
user_bp.route('/register', methods=['POST'])(register)
