"""add content column to posts table

Revision ID: 14de7c5a59f5
Revises: a718fb96cd16
Create Date: 2023-07-02 20:19:59.226851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14de7c5a59f5'
down_revision = 'a718fb96cd16'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
