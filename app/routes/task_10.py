import databases
import psycopg2
from sqlalchemy import create_engine


def connec_to_pg():
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/USR"
    database = databases.Database(SQLALCHEMY_DATABASE_URL)
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    with engine.connect() as conn:
        with open('../files/task10_11/create_tables.sql', 'r') as f:
            query = f.read()
            result = conn.execute(query)
            conn.commit()

        print('таблицы созданы')
