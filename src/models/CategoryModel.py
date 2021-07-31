import datetime
from . import db
from .user import User
from marshmallow import fields, Schema


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    products = db.relationship("ProductModel", backref='category')

    def __init__(self, data):
        self.name = data.get('name')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return CategoryModel.query.all()

    @staticmethod
    def getById(index):
        return CategoryModel.query.get(index)

    @staticmethod
    def getByProductId(index):
        return CategoryModel.query.filter_by(product_id=index).first()
