import uuid

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
    matr = data.generate(file.matrix_size)

    file_id = str(uuid.uuid4())
    path = 'app/files/task6/' + file_id

    if file.file_type == 'json':
        json_writer = JSONWriter()
        json_writer.write(matr, path + '.json')
        #data.to_file(path + '.json', json_data)
    elif file.file_type == 'csv':
        csv_writer = CSVWriter()
        csv_data = csv_writer.write(matr, path + '.csv')
        #data.to_file(path + '.csv', csv_data)
    elif file.file_type == 'yaml':
        yaml_writer = YAMLWriter()
        yaml_data = yaml_writer.write(matr, path + '.yaml')
        #data.to_file(path + '.yaml', yaml_data)
    else:
        raise HTTPException(status_code=400, detail="Введен некоректный тип файла. Введите 'json','csv' или 'yaml'")

    return file_id
