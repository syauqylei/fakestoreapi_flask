import datetime
from . import db
from .user import User
from marshmallow import fields, Schema


class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    product_id = db.relationship('Product', backref='categories', lazy=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    product_id = fields.Int(required=True)
