"""empty message

Revision ID: d1e16d6b8306
Revises: 174cea5d1fda
Create Date: 2024-03-27 10:35:33.006342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1e16d6b8306'
down_revision = '174cea5d1fda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contato',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('mensagem', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contato')
    # ### end Alembic commands ###