"""add year

Revision ID: 06af21695978
Revises: 
Create Date: 2024-05-09 10:05:20.648026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06af21695978'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('year', sa.Integer(), nullable=True))
        batch_op.alter_column('month',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('day',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.alter_column('day',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('month',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('year')

    # ### end Alembic commands ###