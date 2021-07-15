"""empty message

Revision ID: a8e8a048fbfd
Revises: 60dabec947cc
Create Date: 2021-07-14 12:56:47.745926

"""
from alembic import op
import sqlalchemy as sa
import requests

# revision identifiers, used by Alembic.
revision = 'a8e8a048fbfd'
down_revision = '60dabec947cc'
branch_labels = None
depends_on = None

categories_table = sa.sql.table(
    'categories',
    sa.sql.column('id', sa.Integer),
    sa.sql.column('name', sa.String),
)


def upgrade():
    categories = requests.get(
        'https://fakestoreapi.com/products/categories').json()
    dict_categories = [{
        'id': i,
        'name': categories[i]
    } for i in range(len(categories))]
    op.bulk_insert(categories_table, dict_categories)


def downgrade():
    op.drop_table(categories_table)
