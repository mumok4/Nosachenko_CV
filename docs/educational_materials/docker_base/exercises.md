# Практическое задание 1: Развертывание Python кода в Docker контейнере
Цель: Ознакомиться с процессом развертывания приложения на Python в Docker контейнере.

Задачи:

Установка Docker: Убедитесь, что на вашем компьютере установлен Docker. Если нет, следуйте инструкциям на официальном сайте Docker (https://docs.docker.com/get-docker/).

Создание Python приложения: Создайте простое приложение на Python. Например, это может быть "Hello, World!" приложение.

Создание Dockerfile: В папке с вашим Python кодом создайте файл с именем "Dockerfile". В Dockerfile опишите инструкции для создания образа. Например:
```Dockerfile
# Используем базовый образ Python
FROM python:3.9

# Копируем содержимое текущей папки в папку /app в образе
COPY . /app

# Устанавливаем зависимости
RUN pip install -r /app/requirements.txt

# Указываем рабочую директорию
WORKDIR /app

# Запускаем Python приложение
CMD ["python", "app.py"]
```
Создание requirements.txt: Если ваше приложение использует сторонние библиотеки, создайте файл "requirements.txt" и укажите их там.

Сборка Docker образа: В терминале перейдите в папку с Dockerfile и выполните команду для сборки Docker образа:

docker build -t my-python-app .
Где "my-python-app" - это имя образа, а точка означает текущую директорию.

Запуск контейнера: После успешной сборки образа, запустите контейнер командой:

```sh
docker run my-python-app
```
Вы увидите вывод вашего Python приложения в терминале.

Оптимизация Dockerfile: Попробуйте оптимизировать Dockerfile, чтобы уменьшить размер образа. Например, уберите лишние файлы, используйте более легковесные базовые образы и т.д.

Развертывание приложения: Попробуйте изменить ваш Python код и повторите шаги 5-6 для обновления контейнера с новым кодом.

Замечание: Это задание предполагает базовое понимание Docker и Python. Если вы не знакомы с Docker или Python, рекомендуется пройти соответствующие обучающие курсы.

В подавляющем большинстве контейнеров на данный момент используются минимальные образы Linux. Одним из таких примеров является проект Alphine. Подобные миниатюрные сборки ОС позволяют организовать удобную среду для мониторинга приложений и управления ими. Помимо прочего, ОС Linux обладает большим набором эффективных и не требовательных к вычислительным ресурсам инструментов для решения широкого спектра задач. Это и является основной причиной ее выбора при разработке отказоустойчивых, гибких и высоконагруженных решений. Программист, конечно, может запустить код на Python в Docker контейнере без использования образа с ОС, но в случае возникновения ошибки в процессе работы программы или сбоя в работе контейнера зафиксировать его и определить причину сбоя будет достаточно сложно, как и корректно перезапустить работу контейнера, избежав потери данных. Подробней познакомимся с тем, как применять ОС Alphine Linux в образах Docker.



## Практическое задание 2: Развертывание Python кода в Docker контейнере с использованием образа Alpine

Цель: Освоить процесс развертывания приложения на Python в Docker контейнере с использованием образа Alpine Linux.

Задачи:

Установка Docker: Убедитесь, что на вашем компьютере установлен Docker. Если нет, следуйте инструкциям на официальном сайте Docker (https://docs.docker.com/get-docker/).

Создание Python приложения: Напишите простое Python приложение, которое будет выводить "Hello, Docker with Alpine!".

Создание Dockerfile: В папке с вашим Python кодом, создайте файл с именем "Dockerfile". В Dockerfile опишите инструкции для создания Docker образа на основе образа Alpine. Пример Dockerfile:
```Dockerfile
# Используем базовый образ Alpine
FROM python:3.9-alpine

# Копируем содержимое текущей папки в папку /app в образе
COPY . /app

# Устанавливаем зависимости
RUN pip install -r /app/requirements.txt

# Указываем рабочую директорию
WORKDIR /app

# Запускаем Python приложение
CMD ["python", "app.py"]
```
Создание requirements.txt: Если ваше приложение использует сторонние библиотеки, создайте файл "requirements.txt" и укажите их там.

Сборка Docker образа: В терминале, перейдите в папку с Dockerfile и выполните команду для сборки Docker образа:

docker build -t my-python-app-alpine .
Где "my-python-app-alpine" - это имя образа, а точка означает текущую директорию.

Запуск контейнера: После успешной сборки образа, запустите контейнер командой:
```sh
docker run my-python-app-alpine
```
Вы увидите вывод ```Hello, Docker with Alpine!``` в терминале.

Изменение кода: Измените текст вывода вашего Python приложения на "Hello, Docker with Alpine! This is my Alpine containerized app."

Обновление контейнера: Повторите шаги 5-6 для обновления контейнера с новым кодом.

Оптимизация Dockerfile: Попробуйте оптимизировать Dockerfile, чтобы уменьшить размер образа. Уберите лишние файлы и зависимости, используйте более легковесные базовые образы.

Примечание: Это задание предполагает базовое знание Docker и Python. Если вы не знакомы с Docker или Python, рекомендуется предварительно изучить соответствующие темы.