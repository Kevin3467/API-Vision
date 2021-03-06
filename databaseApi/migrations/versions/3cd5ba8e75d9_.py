"""empty message

Revision ID: 3cd5ba8e75d9
Revises: 
Create Date: 2022-05-23 10:57:43.607082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cd5ba8e75d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=sa.TEXT(),
               nullable=True)
    op.drop_constraint('user_username_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_username_key', 'user', ['username'])
    op.alter_column('user', 'username',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###
