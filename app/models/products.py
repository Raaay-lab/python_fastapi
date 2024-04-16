import sqlalchemy

metadata = sqlalchemy.MetaData()

product_table = sqlalchemy.Table(
    "product",
    metadata,
    sqlalchemy.Column("product_name", sqlalchemy.VARCHAR(25), primary_key=True),
    sqlalchemy.Column("product_price", sqlalchemy.NUMERIC(8)),
    sqlalchemy.Column("quantity_on_hand", sqlalchemy.NUMERIC(5)),
    sqlalchemy.Column("laststockdate", sqlalchemy.Date)
)
