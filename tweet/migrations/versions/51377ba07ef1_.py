"""empty message

Revision ID: 51377ba07ef1
Revises: eaff28cbc937
Create Date: 2020-06-26 16:33:24.847656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51377ba07ef1'
down_revision = 'eaff28cbc937'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweets', sa.Column('posted_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tweets', 'posted_at')
    # ### end Alembic commands ###
