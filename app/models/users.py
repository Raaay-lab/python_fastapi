import sqlalchemy

metadata = sqlalchemy.MetaData()


users_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("person_code", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.VARCHAR(15)),
    sqlalchemy.Column("last_name", sqlalchemy.VARCHAR(20)),
    sqlalchemy.Column("hiredate", sqlalchemy.Date)
)
