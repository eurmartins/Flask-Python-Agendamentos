"""Alterando a coluna 'data' para string

Revision ID: 7badf781c6a9
Revises: b599051f63b7
Create Date: 2025-04-01 14:50:06.727018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7badf781c6a9'
down_revision = 'b599051f63b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('agendamento', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data', sa.String(length=10), nullable=True))
        batch_op.alter_column('horario',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=5),
               nullable=True)
        batch_op.alter_column('client',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('servico',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('agendamento', schema=None) as batch_op:
        batch_op.alter_column('servico',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('client',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('horario',
               existing_type=sa.String(length=5),
               type_=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.drop_column('data')

    # ### end Alembic commands ###
