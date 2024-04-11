from fastapi import APIRouter


router = APIRouter(tags=["Стажировка"])
"""
Задание_1. Удаление дублей
    Реализуйте функцию соответствующую следующему описанию:
    На вход подаётся массив слов зависимых от регистра, для которых необходимо произвести
    фильтрацию на основании дублей слов, если в списке найден дубль по регистру, то все
    подобные слова вне зависимости от регистра исключаются.
    На выходе должны получить уникальный список слов в нижнем регистре.

    Список слов для примера: ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']
    Ожидаемый результат: ['папа','брат']
"""


@router.post("/find_in_different_registers", description="Задание_1. Удаление дублей")
async def find_in_different_registers(words: list[str]) -> list[str]:
    """метод для """
    result = []
    count = {}

    for i in words:
        if i in count.keys():
            count[str(i)] = count[str(i)] + 1  # считаю полное кол-во повторяющихся слов
        else:
            count[str(i)] = 1

    for i in count:
        result.append(i.lower())

    result = list(set(result))  # только уникальные слова в нижнем регистре

    temp = []
    # поиск слов с повторяющемся регистром
    for i in result:
        for j in count:
            if i == j.lower() and count[j] > 1:
                temp.append(j.lower())

    # удаление из списка с уникальными словами невалидных слов
    for i in temp:
        result.remove(i)

    return result
