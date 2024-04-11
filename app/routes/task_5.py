import os
import shutil
import uuid

from fastapi import APIRouter, UploadFile, HTTPException
from starlette.responses import FileResponse

from app.core import zip_file

router = APIRouter(tags=["API для хранения файлов"])
"""
Задание_5. API для хранения файлов

a.	Написать API для добавления(POST) "/upload_file" и скачивания (GET) "/download_file/{id}" файлов. 
В ответ на удачную загрузку файла должен приходить id для скачивания. 
b.	Добавить архивирование к post запросу, то есть файл должен сжиматься и сохраняться в ZIP формате.
с*.Добавить аннотации типов.
"""


@router.post("/upload_file", description="Задание_5. API для хранения файлов")
async def upload_file(file: UploadFile):
    """

    """

    path = "app/files/task5"
    file_id = str(uuid.uuid4())
    file_path = os.path.join(path, file_id)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    zip_file(file_path, file.filename)
    os.remove(file_path)

    return {"id": file_id}


@router.get("/download_file/{file_id}", description="Задание_5. API для хранения файлов")
async def download_file(file_id: str):
    """Описание."""
    dir_path = "app/files/task5"
    file_path = os.path.join(dir_path, file_id + ".zip")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, media_type="application/octet-stream", filename=file_id + ".zip")
