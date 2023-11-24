"""create student table

Revision ID: efaa4a99a66a
Revises: 
Create Date: 2023-11-17 08:39:40.461001

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'efaa4a99a66a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('students',
                    sa.Column('id', sa.String, primary_key=True, index=True),
                    sa.Column('name', sa.String),
                    sa.Column('email', sa.String),
                    sa.Column('gpa', sa.String),
                    )


def downgrade() -> None:
    op.drop_table('students')