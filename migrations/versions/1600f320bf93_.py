"""empty message

Revision ID: 1600f320bf93
Revises: 
Create Date: 2023-02-17 22:32:43.222251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1600f320bf93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('body', sa.String(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=32), nullable=True),
    sa.Column('last_name', sa.String(length=32), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('blog')
    # ### end Alembic commands ###