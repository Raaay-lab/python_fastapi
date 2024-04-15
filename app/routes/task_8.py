import json
from functools import wraps
from fastapi import APIRouter

router = APIRouter(tags=["Стажировка"])

"""
Задание_8. Декоратор - счётчик запросов.

Напишите декоратор который будет считать кол-во запросов сделанных к приложению.
Оберните роут new_request() этим декоратором.
Подумать, как хранить переменную с кол-вом сделаных запросов.
"""

file_count_path = 'app/files/task8/request_count.json'


def load_count():
    try:
        with open(file_count_path, "r") as file:
            data = json.load(file)
            return data["count"]
    except FileNotFoundError:
        return 0


def save_count(count):
    data = {"count": count}
    with open(file_count_path, "w") as file:
        json.dump(data, file)


def count_requests(func):
    func.count = load_count()

    @wraps(func)
    async def wrapper(*args, **kwargs):
        func.count += 1
        print(f"Количество запросов: {func.count}")
        save_count(func.count)
        return await func(*args, **kwargs)

    return wrapper


@router.get("/new_request", description="Задание_8. Декоратор - счётчик запросов.")
@count_requests
async def new_request():
    """Возвращает кол-во сделанных запросов."""
    return {'количество запросов': load_count()}
