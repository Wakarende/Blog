"""update post model

Revision ID: f0b78003b7c9
Revises: faf9f898afe1
Create Date: 2021-05-01 14:20:34.386146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0b78003b7c9'
down_revision = 'faf9f898afe1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('posts_author_id_fkey', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['id'])
    op.drop_column('posts', 'author_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('posts_author_id_fkey', 'posts', 'users', ['author_id'], ['id'])
    op.drop_column('posts', 'user_id')
    # ### end Alembic commands ###
