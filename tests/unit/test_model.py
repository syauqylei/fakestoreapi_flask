import pytest
from src.models.ProductModel import ProductModel


@pytest.fixture(scope='module')
def new_product():
    product = ProductModel({
        'title': 'sweater',
        'price': 11.5,
        'image': "https://dummyimage.com/300",
        'description': "really cool sweater for the boys"
    })
    yield product


def test_product(new_product):
    assert new_product.title == 'sweater'
    assert new_product.price == 11.5
    assert new_product.image == "https://dummyimage.com/300"
    assert new_product.description == 'really cool sweater for the boys'
