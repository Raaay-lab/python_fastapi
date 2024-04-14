import logging
import logging.config
import time
from contextvars import ContextVar
from datetime import datetime

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


#logging.config.fileConfig(log_file_path)
logging.basicConfig(filename='app/files/task7/fastapi.log',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(filename)s:%(lineno)d} LOG_LEVEL - %(levelname)s %(message)s")
output_log = logging.getLogger("output")

client_host: ContextVar[str | None] = ContextVar("client_host", default=None)

""" 
Задание_7. Логирование в FastAPI с использованием middleware.
   
Написать конфигурационный файл для логгера "output"
Формат выводимых логов:
[CURRENT_DATETIME] {file: line} LOG_LEVEL - | EXECUTION_TIME_SEC | HTTP_METHOD | URL | STATUS_CODE |
[2023-12-15 00:00:00] {example:62} INFO | 12 | GET | http://localhost/example | 200 |

          
Дописать класс CustomMiddleware.
Добавить middleware в приложение (app).
"""


class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        """Load request ID from headers if present. Generate one otherwise."""
        client_host.set(request.client.host)
        try:
            start_time = time.time()
            response = await call_next(request)
            end_time = time.time()

            output_log.info(f"| {end_time-start_time} | {request.method} | {request.url} | {response.status_code} |")

        except:
            response = Response("Internal Server Error", status_code=500)

        return response
