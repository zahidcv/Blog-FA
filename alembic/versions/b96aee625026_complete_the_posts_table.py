"""complete the posts table

Revision ID: b96aee625026
Revises: 4acc69fab257
Create Date: 2024-04-22 14:32:41.310917

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'b96aee625026'
down_revision: Union[str, None] = '4acc69fab257'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', 
                   sa.Column('created_at', sa.TIMESTAMP(timezone = True), server_default=sa.text('now()'), nullable = False))
    
    op.add_column('posts', 
                   sa.Column('published', sa.Boolean(), server_default='TRUE', nullable = False))


def downgrade() -> None:
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'published')
