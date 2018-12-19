"""empty message

Revision ID: 28a73afcbebd
Revises: 
Create Date: 2018-12-19 10:42:36.687419

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from app.models.cliente_model import Cliente

revision = '28a73afcbebd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clientes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('data_nascimento', sa.DateTime(), nullable=True),
    sa.Column('profissao', sa.String(length=30), nullable=True),
    sa.Column('sexo', sqlalchemy_utils.types.choice.ChoiceType(Cliente.SEXO_CHOICES), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clientes')
    # ### end Alembic commands ###
