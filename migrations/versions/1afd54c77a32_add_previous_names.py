"""Add previous_names

Revision ID: 1afd54c77a32
Revises: 2864e71a466e
Create Date: 2020-08-12 15:13:09.682717

"""

# revision identifiers, used by Alembic.
revision = '1afd54c77a32'
down_revision = '2864e71a466e'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


def upgrade():
    op.add_column('organization', sa.Column('previous_names', JSONB(), nullable=True))


def downgrade():
    op.drop_column('organization', 'previous_names')
