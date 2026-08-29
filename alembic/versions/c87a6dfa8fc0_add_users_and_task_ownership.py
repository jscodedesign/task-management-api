"""add users and task ownership

Revision ID: c87a6dfa8fc0
Revises: 02bc774808e0
Create Date: 2026-08-28 14:02:22.687377
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c87a6dfa8fc0"
down_revision: Union[str, Sequence[str], None] = "02bc774808e0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_users_username"),
        "users",
        ["username"],
        unique=True,
    )

    op.add_column(
        "tasks",
        sa.Column("user_id", sa.Integer(), nullable=True),
    )

    op.create_foreign_key(
        "fk_tasks_user_id",
        "tasks",
        "users",
        ["user_id"],
        ["id"],
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        "fk_tasks_user_id",
        "tasks",
        type_="foreignkey",
    )

    op.drop_column("tasks", "user_id")

    op.drop_index(
        op.f("ix_users_username"),
        table_name="users",
    )

    op.drop_table("users")