"""Seed dogs table in demo.db

Revision ID: 54076c209000
Revises: 1ff61db49dff
Create Date: 2024-05-23 11:11:52.005485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from seed import delete_records, create_dogs

# revision identifiers, used by Alembic.
revision: str = '54076c209000'
down_revision: Union[str, None] = '1ff61db49dff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    delete_records()
    create_dogs(30)


def downgrade() -> None:
    delete_records()
