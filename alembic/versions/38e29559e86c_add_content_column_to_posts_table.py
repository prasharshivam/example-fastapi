"""add content column to posts table

Revision ID: 38e29559e86c
Revises: 8c127c9503a3
Create Date: 2025-11-23 08:16:42.058609

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38e29559e86c'
down_revision: Union[str, Sequence[str], None] = '8c127c9503a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
