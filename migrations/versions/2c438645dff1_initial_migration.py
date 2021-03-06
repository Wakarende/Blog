"""initial migration

Revision ID: 2c438645dff1
Revises: 
Create Date: 2021-05-01 15:12:03.216222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c438645dff1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('post_content', sa.String(), nullable=True),
    sa.Column('short_description', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
