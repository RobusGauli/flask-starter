"""empty message

Revision ID: 26666d6b0354
Revises: 6daba961ed58
Create Date: 2018-06-07 19:19:53.318482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26666d6b0354'
down_revision = '6daba961ed58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('address', sa.String(length=300), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'address')
    # ### end Alembic commands ###