"""empty message

Revision ID: a46a32d62d97
Revises: 
Create Date: 2018-10-25 02:56:31.562772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a46a32d62d97'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('interests', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('starttime', sa.String(), nullable=True),
    sa.Column('endtime', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('interests', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['email'], ['users.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    op.drop_table('users')
    # ### end Alembic commands ###