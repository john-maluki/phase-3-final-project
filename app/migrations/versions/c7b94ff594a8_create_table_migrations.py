"""Create table migrations

Revision ID: c7b94ff594a8
Revises: 
Create Date: 2023-09-06 15:35:42.566798

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7b94ff594a8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adopters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fisrt_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('facility_id', sa.Integer(), nullable=False),
    sa.Column('adopter_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['adopter_id'], ['adopters.id'], ),
    sa.ForeignKeyConstraint(['facility_id'], ['facilities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dogs')
    op.drop_table('facilities')
    op.drop_table('adopters')
    # ### end Alembic commands ###