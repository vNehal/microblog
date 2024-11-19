"""Fix models for Bookmark functionality

Revision ID: 712573a7620e
Revises: 425ffdecd897
Create Date: 2024-11-19 04:35:51.361274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '712573a7620e'
down_revision = '425ffdecd897'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bookmark', schema=None) as batch_op:
        # Add new columns
        batch_op.add_column(sa.Column('post_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_bookmark_timestamp'), ['timestamp'], unique=False)

        # Drop the old column without dropping the non-existent constraint
        batch_op.drop_column('review_id')

        # Add the new foreign key
        batch_op.create_foreign_key(batch_op.f('fk_bookmark_post_id_post'), 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bookmark', schema=None) as batch_op:
        # Revert changes
        batch_op.add_column(sa.Column('review_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint(batch_op.f('fk_bookmark_post_id_post'), type_='foreignkey')
        batch_op.drop_column('post_id')
        batch_op.drop_index(batch_op.f('ix_bookmark_timestamp'))
        batch_op.drop_column('timestamp')

        # Add back the original foreign key
        batch_op.create_foreign_key(batch_op.f('fk_bookmark_review_id_post'), 'post', ['review_id'], ['id'])
    # ### end Alembic commands ###

