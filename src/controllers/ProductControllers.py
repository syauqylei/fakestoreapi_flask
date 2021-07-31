import json
from flask import request, jsonify
from src.models.ProductModel import ProductModel
from src.models.CategoryModel import CategoryModel
from src.shared.Authentication import Auth
from src.schemas import *

products_schema = ProductSchema(many=True)
product_schema = ProductSchema()


@Auth.auth_required
def get_all():
    try:
        products = ProductModel.get_all()

        data = products_schema.dump(products)
        return jsonify(data), 200
    except Exception:
        print(Exception)
        return jsonify({'message': "Internal Server Error"}), 500


@Auth.auth_required
def get_one(product_id):
    try:
        product = ProductModel.get_one(product_id)
        data = product_schema.dump(product)

        return jsonify(data), 200
    except:
        return jsonify({'message': "Internal Server Error"}), 500


@Auth.auth_required
def get_category():
    try:
        category_schema = CategorySchema(many=True)
        categories = CategoryModel.get_all()
        data = category_schema.dump(categories)

        return jsonify(data), 200
    except:
        return jsonify({'message': "Internal Server Error"}), 500
