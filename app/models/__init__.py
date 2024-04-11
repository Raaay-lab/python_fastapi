import re
from typing import Union

from pydantic import BaseModel, ConfigDict, validator, model_validator


class File(BaseModel):
    file_type: str
    matrix_size: int


class ConverterRequest(BaseModel):
    number: Union[int, str]


class ConverterResponse(BaseModel):
    arabic: int
    roman: str


class User(BaseModel):
    name: str
    age: int
    adult: Union[bool, None] = None
    message: Union[str, None] = None


    """
    проверка на совершеннолетие
    """
    @model_validator(mode='after')
    def check_adult(self) -> 'User':
        age = self.age
        if age <= 0:
            raise ValueError('Введите возраст > 0')
        elif 0 < age < 18:
            self.adult = False
            return self
        elif 18 <= age < 100:
            self.adult = True
            return self
        else:
            raise ValueError('Вам слишком много лет')


class MetaMapping(BaseModel):
    list_of_ids: list
    tags: list[str]


class Meta(BaseModel):
    last_modification: str
    list_of_skills: Union[list[str], None] = None
    mapping: MetaMapping
    """
    Проверка на соответствие формату.
    Пока не полностью покрывает все даты те могут быть примеры вида 00/15/2021
    Т.е. день и месяц неверные
    """
    @model_validator(mode='after')
    def check_last_mod(self) -> 'Meta':
        date = self.last_modification
        if re.fullmatch(re.compile(r'[0-3]\d/[0-1]\d/\d{4}'), date):
            return self
        else:
            raise ValueError('Дата в неверном формате')


class BigJson(BaseModel):
    """Использует модель User."""
    user: User
    meta: Meta
