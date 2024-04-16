import sqlalchemy
from .users import users_table
from .products import product_table

metadata = sqlalchemy.MetaData()

purchase_table = sqlalchemy.Table(
    "purchase",
    metadata,
    sqlalchemy.Column("product_name", sqlalchemy.ForeignKey(product_table.c.product_name)),
    sqlalchemy.Column("salesperson", sqlalchemy.ForeignKey(users_table.c.person_code)),
    sqlalchemy.Column("purchase_date", sqlalchemy.Date),
    sqlalchemy.Column("quantity", sqlalchemy.NUMERIC)
)
