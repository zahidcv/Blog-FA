"""add content column

Revision ID: 3625e07dd1ea
Revises: b0680bfeed3f
Create Date: 2024-04-22 14:08:53.250750

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '3625e07dd1ea'
down_revision: Union[str, None] = 'b0680bfeed3f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
