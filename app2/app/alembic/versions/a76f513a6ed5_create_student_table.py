"""create student table

Revision ID: a76f513a6ed5
Revises: efaa4a99a66a
Create Date: 2023-11-17 09:45:22.568448

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a76f513a6ed5'
down_revision: Union[str, None] = 'efaa4a99a66a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('students',
                    sa.Column('id', sa.Integer, primary_key=True, index=True),
                    sa.Column('name', sa.String),
                    sa.Column('email', sa.String),
                    sa.Column('gpa', sa.String),
                    )


def downgrade() -> None:
    op.drop_table('students')