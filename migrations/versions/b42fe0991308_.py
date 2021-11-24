"""empty message

Revision ID: b42fe0991308
Revises: d16481a34eaa
Create Date: 2021-11-21 20:53:48.927184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b42fe0991308'
down_revision = 'd16481a34eaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rating', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rating', 'id')
    # ### end Alembic commands ###
