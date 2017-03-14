"""empty message

Revision ID: b27ead8cc832
Revises: 63e1884256b7
Create Date: 2017-03-14 03:26:59.121764

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b27ead8cc832'
down_revision = '63e1884256b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=80), nullable=True),
    sa.Column('lname', sa.String(length=80), nullable=True),
    sa.Column('user', sa.String(length=80), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gen', sa.String(length=6), nullable=True),
    sa.Column('bio', sa.String(length=200), nullable=True),
    sa.Column('img', sa.String(length=256), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('user')
    )
    op.drop_table('user_profile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('fname', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('lname', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('user', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('gen', sa.VARCHAR(length=6), autoincrement=False, nullable=True),
    sa.Column('bio', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('img', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'user_profile_pkey'),
    sa.UniqueConstraint('user', name=u'user_profile_user_key')
    )
    op.drop_table('profiles')
    # ### end Alembic commands ###
