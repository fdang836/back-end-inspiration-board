"""added color and defaultPos

Revision ID: bd22f391d3b1
Revises: 0a9388b51699
Create Date: 2022-07-17 15:36:54.972547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd22f391d3b1'
down_revision = '0a9388b51699'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('color', sa.String(), nullable=True))
    op.add_column('card', sa.Column('defaultPos', sa.PickleType(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card', 'defaultPos')
    op.drop_column('card', 'color')
    # ### end Alembic commands ###
