import json
from flask import request, jsonify
from src.models.ProductModel import ProductModel, ProductSchema

products_schema = ProductSchema(many=True)
product_schema = ProductSchema()


def get_all():
    try:
        products = ProductModel.get_all()

        data = products_schema.dump(products)
        return jsonify(data), 200
    except Exception:
        print(Exception)
        return jsonify({'message': "Internal Server Error"}), 500


def get_one(pk):
    try:
        product = ProductModel.get_one(pk)
    except:
        return jsonify({'message': "Internal Server Error"}), 500

    data = product_schema.dump(product)
    return jsonify(data), 200
