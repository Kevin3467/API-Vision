"""empty message

Revision ID: 1009f4a549b5
Revises: aa43e1b30c6a
Create Date: 2022-06-07 11:41:51.115783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1009f4a549b5'
down_revision = 'aa43e1b30c6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chamados', 'textteste')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chamados', sa.Column('textteste', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
