"""Initial migration

Revision ID: cd87e7c2f5f2
Revises: 
Create Date: 2024-11-20 16:55:37.379987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd87e7c2f5f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('pair',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student1_id', sa.Integer(), nullable=False),
    sa.Column('student2_id', sa.Integer(), nullable=False),
    sa.Column('week', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['student1_id'], ['student.id'], ),
    sa.ForeignKeyConstraint(['student2_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pair')
    op.drop_table('user')
    op.drop_table('student')
    # ### end Alembic commands ###