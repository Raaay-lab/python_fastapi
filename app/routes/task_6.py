from fastapi import APIRouter, HTTPException

from app.core import DataGenerator, JSONWriter, CSVWriter, YAMLWriter
from app.models import File

router = APIRouter(tags=["API для хранения файлов"])
"""
Задание_6. 

Изучите следущие классы в модуле app.core: BaseWriter, DataGenerator

API должно принимать json, по типу:
{
    "file_type": "json",  # или "csv", "yaml"
    "matrix_size": int    # число от 4 до 15
}
В ответ на удачную генерацию файла должен приходить id для скачивания.

Добавьте реализацию методов класса DataGenerator.
Добавьте аннотации типов и (если требуется) модели в модуль app.models.

(Подумать, как переисползовать код из задания 5)
"""


@router.post("/generate_file", description="Задание_6. Конвертер")
async def generate_file(file: File) -> str:
    """Описание."""

    data = DataGenerator()
    mart = data.generate(file.matrix_size)
    path = 'app/files/task6'

    json_writer = JSONWriter()
    xx = json_writer.write(mart)
    print(xx)

    if file.file_type == 'json':
        data.to_file(path, json_writer)
    elif file.file_type == 'csv':
        data.to_file(path, CSVWriter.write())
    elif file.file_type == 'yaml':
        data.to_file(path, YAMLWriter.write())
    else:
        raise HTTPException(status_code=400, detail="Введен некоректный тип файла. Введите 'json','csv' или 'yaml'")
    file_id: str = data.file_id

    return "file_id"
