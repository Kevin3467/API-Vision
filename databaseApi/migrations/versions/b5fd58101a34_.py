"""empty message

Revision ID: b5fd58101a34
Revises: 80a5ec8ab2b8
Create Date: 2022-05-23 11:32:09.876403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5fd58101a34'
down_revision = '80a5ec8ab2b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orcamentos', sa.Column('orcstatus', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orcamentos', 'orcstatus')
    # ### end Alembic commands ###
