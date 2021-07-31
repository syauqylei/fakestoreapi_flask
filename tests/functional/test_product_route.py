import pytest
import json
from src.schemas import *
from src.models.ProductModel import ProductModel
from src.models.CategoryModel import CategoryModel
from src.models.user import User


@pytest.fixture(scope="module")
def seed_product():
    category = CategoryModel({'name': 'computer accesories'})
    product1 = ProductModel({
        'title': 'mouse gg',
        'description': 'computer',
        'price': 14,
        'image': 'https://dummyimage.com/300'
    })
    product2 = ProductModel({
        'title': 'keyboard gg',
        'description': 'computer',
        'price': 14,
        'image': 'https://dummyimage.com/300'
    })
    product3 = ProductModel({
        'title': 'monitor gg',
        'description': 'computer monitor',
        'price': 100,
        'image': 'https://dummyimage.com/300'
    })

    user = User({
        'name': 'admin',
        'email': 'admin@mail.com',
        'password': 'password'
    })
    category.products.append(product3)
    category.products.append(product2)
    category.products.append(product1)

    product3.save()
    product2.save()
    product1.save()
    category.save()

    yield ProductModel.get_all()
    product3.delete()
    product2.delete()
    product1.delete()

    category.delete()


@pytest.fixture(scope="module")
def get_access(test_client):
    user = User({
        'name': 'sigantengkalem',
        'email': 'sigantengono@mail.com',
        'password': 'password'
    })
    user.save()

    res = test_client.post('/api/login',
                           data=json.dumps(
                               dict(email='sigantengono@mail.com',
                                    password='password')),
                           content_type='application/json')

    res_json = res.get_json()
    access_token = res_json['access_token']

    yield access_token

    user.delete()


def test_without_access_token(test_client):
    response = test_client.get('/api/products',
                               headers={
                                   'Content-Type': 'application/json',
                               })

    resData = response.get_json()

    assert response.status == "403 FORBIDDEN"
    assert "error" in resData
    assert resData['error'] == "You dont have the credential to use this API"


def test_get_all_product(test_client, seed_product, get_access):

    response = test_client.get('/api/products',
                               headers={
                                   'Content-Type': 'application/json',
                                   'access_token': get_access
                               })
    resData = response.get_json()

    data = ProductModel.get_all()
    serializer = ProductSchema(many=True)
    serialized_data = serializer.dump(data)

    assert response.status == "200 OK"
    assert resData == serialized_data


def test_get_one(test_client, seed_product, get_access):

    response = test_client.get('/api/products/1',
                               headers={
                                   'Content-Type': 'application/json',
                                   'access_token': get_access
                               })
    resData = response.get_json()

    data = ProductModel.get_one(1)
    serializer = ProductSchema()
    serialized_data = serializer.dump(data)

    assert response.status == "200 OK"
    assert resData == serialized_data


def test_get_all_category(test_client, seed_product, get_access):
    response = test_client.get('/api/category',
                               headers={
                                   'Content-Type': 'application/json',
                                   'access_token': get_access
                               })
    resData = response.get_json()
    data = CategoryModel.get_all()
    serializer = CategorySchema(many=True)
    serialized_data = serializer.dump(data)

    assert response.status == "200 OK"
    assert resData == serialized_data
