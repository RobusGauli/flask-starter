"""
    Create users table.

    Revision ID: c4de12ecee61
    Revises: 265aa8a29f5e
    Create Date: 2018-06-04 15:57:18.431836
"""
import datetime
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'c4de12ecee61'
down_revision = '265aa8a29f5e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False, unique=True),
        sa.Column('password', sa.String(50), nullable=False),
        sa.Column('role_id', sa.Integer),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
        sa.Column('create_at', sa.DateTime, default=datetime.datetime.now),
        sa.Column('updated_at', sa.DateTime, onupdate=datetime.datetime.now),
    )


def downgrade():
    op.drop_table('users')
