from marshmallow import Schema, fields


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    price = fields.Float()
    description = fields.Str()
    image = fields.Str()
    created_at = fields.DateTime()
    modified_at = fields.DateTime()


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
