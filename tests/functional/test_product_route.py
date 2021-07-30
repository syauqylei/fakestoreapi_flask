import pytest
import json
from src.models.ProductModel import ProductModel, ProductSchema
from src.models.CategoryModel import CategoryModel
from src.models.user import User


@pytest.fixture(scope="module")
def seed_product():
    category = CategoryModel({'name': 'computer accesories'})
    product1 = ProductModel({
        'title': 'mouse gg',
        'descrption': 'computer',
        'price': 14,
        'image': 'https://dummyimage.com/300'
    })
    product2 = ProductModel({
        'title': 'keyboard gg',
        'descrption': 'computer',
        'price': 14,
        'image': 'https://dummyimage.com/300'
    })
    product3 = ProductModel({
        'title': 'monitor gg',
        'descrption': 'computer monitor',
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


def test_get_all_product(test_client, seed_product):

    loginRes = test_client.post('/api/login',
                                data=json.dumps(
                                    dict(email='rindu@mail.com',
                                         password='password')),
                                content_type='application/json')

    loginData = loginRes.get_json()

    response = test_client.get('/api/products',
                               headers={
                                   'Content-Type': 'application/json',
                                   'access_token': loginData
                               })
    resData = response.get_json()

    data = ProductModel.get_all()
    serializer = ProductSchema(many=True)
    serialized_data = serializer.dump(data)

    assert response.status == "200 OK"
    assert resData == serialized_data
