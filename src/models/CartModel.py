class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    product_id = db.relationship('Product', backref='categories', lazy=True)


carts = db.Table('carts',
                 db.Column('product_id',
                           db.Integer,
                           db.ForeignKey('product.id'),
                           primary_key=True),
                 db.Column('user_id'),
                 db.Integer,
                 db.ForeignKey('user.id'),
                 primary_key=True)
