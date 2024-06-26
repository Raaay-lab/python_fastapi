# education

### Установка [poetry](https://python-poetry.org/)

Есть несколько способов установки poetry. Проще всего установить так:

`pip install poetry`

Если этот способ не подойдёт по какой-то причине, то на официальном сайте также описаны другие способы [установки](https://python-poetry.org/docs/#installing-with-the-official-installer).

Важно, чтобы путь к poetry был прописан в PATH


### Настройка виртуального окружения

Poetry работает с виртуальными окружениями. При этом он изначально настроен так, что у вас будет много разных версий Python. По этой причине инструмент создает виртуальные окружения для проектов в непривычном месте. Посмотреть, где poetry размещает виртуальные окружения, можно командой:

`poetry config --list`

В выводе этой команды нас интересует строка virtualenvs.path.

Чтобы настроить размещение виртуальных окружений в папках проектов нужно выполнить команду:

`poetry config virtualenvs.in-project true`


### Инициализация виртуального окружения

`poetry install`

Эта команда устанавливает все зависимости в окружение в директорию .venv проекта. 

Активируется окружение командой poetry shell, а завершается командой exit.
Обычно активация окружения необязательна — Poetry предлагает команду run, которая исполняет программы уже изнутри окружения. Например, poetry run python.


# Docker

создать файл с пакетами:
`pip freeze > requirements.txt`

построить образ приложения:
`docker build -t task9 .`

запустить контейнер на 80 порту:
`docker run -d --name task9container -p 80:80 task9`