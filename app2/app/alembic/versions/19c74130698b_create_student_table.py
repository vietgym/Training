"""create student table

Revision ID: 19c74130698b
Revises: 5ecb25c556eb
Create Date: 2023-11-17 09:58:19.282400

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19c74130698b'
down_revision: Union[str, None] = '5ecb25c556eb'
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