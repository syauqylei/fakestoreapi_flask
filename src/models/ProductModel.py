import datetime
from . import db
from .user import User
from src.models.CategoryModel import CategoryModel


class ProductModel(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.title = data.get('title')
        self.price = data.get('price')
        self.description = data.get('description')
        self.image = data.get('image')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)

        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return ProductModel.query.all()

    @staticmethod
    def get_one(index):
        return ProductModel.query.get(index)
