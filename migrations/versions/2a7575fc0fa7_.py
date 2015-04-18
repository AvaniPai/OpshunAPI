"""empty message

Revision ID: 2a7575fc0fa7
Revises: None
Create Date: 2015-03-28 01:31:34.506155

"""

# revision identifiers, used by Alembic.
revision = '2a7575fc0fa7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userinfo')
    ### end Alembic commands ###