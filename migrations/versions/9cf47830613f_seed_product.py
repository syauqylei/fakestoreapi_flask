"""seed_product

Revision ID: 9cf47830613f
Revises: a8e8a048fbfd
Create Date: 2021-07-14 13:25:00.425200

"""
from alembic import op
import sys

sys.path.append('../..')
from src.models import CategoryModel
import datetime
import sqlalchemy as sa
import requests

# revision identifiers, used by Alembic.
revision = '9cf47830613f'
down_revision = 'a8e8a048fbfd'
branch_labels = None
depends_on = None

product_table = sa.sql.table(
    'categories',
    sa.sql.column('id', sa.Integer),
    sa.sql.column('name', sa.String),
)


def upgrade():
    product = requests.get('https://fakestoreapi.com/products').json()

    for item in product:
        item['category_id'] = CategoryModel.CategoryModel.query.filter(
            name=item['category']).first().id
        del item['category']
    op.bulk_insert(product_table, product)


def downgrade():
    pass
