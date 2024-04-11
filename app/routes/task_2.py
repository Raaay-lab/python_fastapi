from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from app.core import convert_arabic_to_roman, convert_roman_to_arabic
from app.models import ConverterResponse, ConverterRequest

router = APIRouter(tags=["Стажировка"])
"""
Задание_2. Конвертер
    1. Реализовать функции convert_arabic_to_roman() и convert_roman_to_arabic() из пакета app.core
    2. Написать логику и проверки для вводимых данных. Учитывать, что если арабское число выходит за пределы 
    от 1 до 3999, то возвращать "не поддерживается"
    3. Запустить приложение и проверить результат через swagger
"""


@router.post("/converter", description="Задание_2. Конвертер")
async def convert_number(number: Annotated[int | str, Body()]) -> ConverterResponse:
    """
    Принимает арабское или римское число.
    Конвертирует его в римское или арабское соответственно.
    Возвращает первоначальное и полученное числа в виде json:
    {
        "arabic": 10,
        "roman": "X"
    }
    """
    try:
        if type(number) == int:
            converter_response = ConverterResponse(arabic=number, roman=convert_arabic_to_roman(number))
            return converter_response
        elif type(number) == str:
            converter_response = ConverterResponse(arabic=convert_roman_to_arabic(number), roman=number)
            return converter_response
    except:
        raise HTTPException(status_code=404,
                            detail="Введите римское число состоящее из букв 'I', 'V', 'X', 'L', 'C', 'D', 'M' или "
                                   "арабское число в промежутке (0:3999)")
