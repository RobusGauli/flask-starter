"""
    Create roles table.

    Revision ID: 265aa8a29f5e
    Revises:
    Create Date: 2018-06-04 15:57:15.100982
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '265aa8a29f5e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.String(50), nullable=False)
    )


def downgrade():
    op.drop_table('roles')
