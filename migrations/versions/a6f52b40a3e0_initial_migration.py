"""Initial migration

Revision ID: a6f52b40a3e0
Revises: 
Create Date: 2023-07-26 18:44:29.598999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6f52b40a3e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('productid', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('productid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###