"""rename todos table to tasks

Revision ID: 02bc774808e0
Revises: 4f844b49b588
Create Date: 2026-08-27 15:11:30.595878

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '02bc774808e0'
down_revision: Union[str, Sequence[str], None] = '4f844b49b588'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('todos', 'tasks')


def downgrade() -> None:
    op.rename_table('tasks', 'todos')
