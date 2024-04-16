import databases
from fastapi import APIRouter
from sqlalchemy import select, delete, insert, engine, create_engine, update
from app.models import UserTable
from app.models.users import users_table

router = APIRouter(tags=["Стажировка"])
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/USR"
database = databases.Database(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

@router.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()


@router.post("/add_users")
async def add_users(user: UserTable):

    query = (
        insert(users_table).values(person_code=user.person_code,
                                   first_name=user.first_name,
                                   last_name=user.last_name,
                                   hiredate=user.hiredate)
    )

    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()

    return f"Пользователь {user.first_name} {user.last_name} добавлен"


@router.get("/get_users/{user_id}")
async def get_users(user_id: int):
    query = (
        select(
            users_table.c.person_code,
            users_table.c.first_name,
            users_table.c.last_name,
            users_table.c.hiredate
        ).where(users_table.c.person_code == user_id)
    )
    a = await database.fetch_all(query)

    result = {}
    for record in a:
        result = {
            "person_code": record["person_code"],
            "first_name": record["first_name"],
            "last_name": record["last_name"],
            "hiredate": record["hiredate"]
        }

    return result


@router.put("/upd_users")
async def add_users(user: UserTable):
    query = (
        update(users_table).
        where(users_table.c.person_code == user.person_code).
        values(first_name=user.first_name,
               last_name=user.last_name,
               hiredate=user.hiredate)
    )

    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()

    return f"Пользователь {user.first_name} {user.last_name} обновлен"


@router.delete("/del_users/{user_id}")
async def del_users(user_id: int):
    query = (
        delete(users_table).where(users_table.c.person_code == user_id)
    )
    await database.fetch_all(query)

    return "Удаление успешно завершено"
