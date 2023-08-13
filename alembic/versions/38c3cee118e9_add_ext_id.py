"""add ext id

Revision ID: 38c3cee118e9
Revises: 7d63f5358cf3
Create Date: 2023-08-13 00:39:50.215366

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = '38c3cee118e9'
down_revision = '7d63f5358cf3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('spatial_ref_sys')
    op.add_column('events', sa.Column('ext_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'ext_id')
    # op.create_table('spatial_ref_sys',
    # sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    # sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    # sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    # sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    # sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    # )
    # ### end Alembic commands ###
