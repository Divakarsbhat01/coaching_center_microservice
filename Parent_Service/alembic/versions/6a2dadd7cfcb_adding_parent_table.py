"""Adding parent table

Revision ID: 6a2dadd7cfcb
Revises: 
Create Date: 2024-02-27 15:57:35.805934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a2dadd7cfcb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Parent',
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=False),
    sa.Column('email_id', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('parent_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Parent')
    # ### end Alembic commands ###