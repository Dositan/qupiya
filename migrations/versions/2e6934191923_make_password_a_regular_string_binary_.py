"""Make password a regular String: Binary makes no sense

Revision ID: 2e6934191923
Revises: 7bb07654c42c
Create Date: 2022-02-13 12:17:01.401897

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2e6934191923'
down_revision = '7bb07654c42c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('records', 'password',
               existing_type=postgresql.VARCHAR(128),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('records', 'password',
               existing_type=postgresql.BYTEA(),
               nullable=True)
    # ### end Alembic commands ###