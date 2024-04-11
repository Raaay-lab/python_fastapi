import math
from random import randint
import zipfile
from abc import ABC, abstractmethod
from io import StringIO

alf = {"I": 1,
       "V": 5,
       "X": 10,
       "L": 50,
       "C": 100,
       "D": 500,
       "M": 1000}

collision = {
    ('I', 'V'): 3,
    ('I', 'X'): 8,
    ('X', 'L'): 30,
    ('X', 'C'): 80,
    ('C', 'D'): 300,
    ('C', 'M'): 800,
}


def convert_arabic_to_roman(number: int) -> str:
    """

    """
    roman = "I" * number

    roman = roman.replace("I" * 5, "V")
    roman = roman.replace("V" * 2, "X")
    roman = roman.replace("X" * 5, "L")
    roman = roman.replace("L" * 2, "C")
    roman = roman.replace("C" * 5, "D")
    roman = roman.replace("D" * 2, "M")

    roman = roman.replace("DCCCC", "CM")
    roman = roman.replace("CCCC", "CD")
    roman = roman.replace("LXXXX", "XC")
    roman = roman.replace("XXXX", "XL")
    roman = roman.replace("VIIII", "IX")
    roman = roman.replace("IIII", "IV")
    return roman


def convert_roman_to_arabic(number: str) -> int:
    """

    """
    arabic = 0
    prev_literal = None
    for literal in number:
        if prev_literal and alf[prev_literal] < alf[literal]:
            arabic += collision[(prev_literal, literal)]
        else:
            arabic += alf[literal]
        prev_literal = literal
    return arabic


async def is_valid_csv(file_name, df) -> bool:
    """
    Проверка файла на валидность.
    Проверка формата файла и названий столбцов.
    """
    f_name = str(file_name).split(".")
    if f_name[-1] != 'csv':
        return False

    cols_names = ['Имя', 'Возраст', 'Должность']
    for col in df.columns:
        if col not in cols_names:
            return False

    return True


async def average_age_by_position(df):
    """
    вычисление среднего возраста работников на позициях
    """
    df['Возраст'].fillna(df['Возраст'], inplace=True)
    result = df.groupby("Должность")["Возраст"].mean().to_dict()
    for i in result:
        if math.isnan(result[i]):
            result[i] = None
    return result


def zip_file(file_path, original_filename):
    zip_file_path = file_path + '.zip'
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zip_info = zipfile.ZipInfo(original_filename)
        zip_info.filename = original_filename
        zipf.write(file_path, arcname=original_filename)
    return zip_file_path


"""
Задание_6.
Дан класс DataGenerator, который имеет два метода: generate(), to_file()
Метод generate генерирует данные формата list[list[int, str, float]] и записывает результат в
переменную класса data
Метод to_file сохраняет значение переменной generated_data по пути path c помощью метода
write, классов JSONWritter, CSVWritter, YAMLWritter.

Допишите реализацию методов и классов.
"""


class BaseWriter(ABC):
    """Абстрактный класс с методом write для генерации файла"""

    @abstractmethod
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        """
        Записывает данные в строковый объект файла StringIO
        :param data: полученные данные
        :return: Объект StringIO с данными из data
        """
        pass


class JSONWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в json формате"""
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        """Ваша реализация"""
        s = StringIO()
        s.write(str(data))
        return s


class CSVWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в csv формате"""
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        """Ваша реализация"""

        pass


class YAMLWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в yaml формате"""
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        """Ваша реализация"""
        pass


class DataGenerator:
    def __init__(self, data: list[list[int, str, float]] = None):
        self.data: list[list[int, str, float]] = data
        self.file_id = None

    def generate(self, matrix_size) -> list[list[int, str, float]]:
        """Генерирует матрицу данных заданного размера."""

        data: list[list[int, str, float]] = []
        """Ваша реализация"""
        for i in range(matrix_size):
            data2 = []
            for j in range(matrix_size):
                data2.append(randint(0, 100))

            data.append(data2)
        self.data = data
        return data

    def to_file(self, path: str, writer) -> None:
        """
        Метод для записи в файл данных полученных после генерации.
        Если данных нет, то вызывается кастомный Exception.
        :param path: Путь куда требуется сохранить файл
        :param writer: Одна из реализаций классов потомков от BaseWriter
        """

        """Ваша реализация"""
        with open(path+'/json.json', 'w') as f:
            f.write(writer)
