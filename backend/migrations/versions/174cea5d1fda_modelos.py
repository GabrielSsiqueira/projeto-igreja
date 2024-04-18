"""modelos

Revision ID: 174cea5d1fda
Revises: 
Create Date: 2024-03-14 23:15:13.277025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '174cea5d1fda'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('atas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=True),
    sa.Column('tipo', sa.String(length=100), nullable=True),
    sa.Column('presidente_secao', sa.String(length=30), nullable=True),
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('membros_presentes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('membros',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('idade', sa.Integer(), nullable=True),
    sa.Column('nascimento', sa.Date(), nullable=True),
    sa.Column('sexo', sa.String(length=20), nullable=True),
    sa.Column('cpf', sa.String(length=20), nullable=True),
    sa.Column('rg', sa.String(length=15), nullable=True),
    sa.Column('e_civil', sa.String(length=100), nullable=True),
    sa.Column('cidade_estado', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('rg')
    )
    op.create_table('lideranca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('presidente', sa.String(length=100), nullable=True),
    sa.Column('vice_presidente', sa.String(length=100), nullable=True),
    sa.Column('secretario', sa.String(length=100), nullable=True),
    sa.Column('vice_secretario', sa.String(length=100), nullable=True),
    sa.Column('tesoureiro', sa.String(length=100), nullable=True),
    sa.Column('vice_tesoureiro', sa.String(length=100), nullable=True),
    sa.Column('membros_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['membros_id'], ['membros.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lideranca')
    op.drop_table('membros')
    op.drop_table('atas')
    # ### end Alembic commands ###
