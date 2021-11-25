"""empty message

Revision ID: 354347cc02d4
Revises: 61c09ad1f636
Create Date: 2021-11-21 19:16:21.572864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '354347cc02d4'
down_revision = '61c09ad1f636'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rating', sa.Column('point', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'rating', 'books', ['book_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rating', type_='foreignkey')
    op.drop_column('rating', 'point')
    # ### end Alembic commands ###