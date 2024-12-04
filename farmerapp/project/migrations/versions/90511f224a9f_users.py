"""USers

Revision ID: 90511f224a9f
Revises: 8c5b1b69dd97
Create Date: 2024-08-09 09:47:59.159233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90511f224a9f'
down_revision = '8c5b1b69dd97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.TEXT(),
               type_=sa.String(length=256),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=256),
               type_=sa.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
