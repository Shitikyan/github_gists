"""Init

Revision ID: 4cb7e442138b
Revises: 
Create Date: 2022-08-25 18:52:32.506717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb7e442138b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'gist_request',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(1024)),
        sa.Column('at', sa.TIMESTAMP(), server_default=sa.func.current_timestamp())
        )


def downgrade():
    op.drop_table('gist_request')
