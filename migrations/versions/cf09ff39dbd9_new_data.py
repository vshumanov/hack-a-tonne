"""new data

Revision ID: cf09ff39dbd9
Revises: 82c2c0bc8160
Create Date: 2018-05-12 16:25:38.899871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf09ff39dbd9'
down_revision = '82c2c0bc8160'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('picture', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'picture')
    op.drop_column('user', 'phone')
    # ### end Alembic commands ###