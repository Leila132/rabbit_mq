# rabbit_mq

Проект, в котором осуществляется логирование через RabbitMQ. Файл producer.py имитирует поведение некой системы, которая отправляет логи в RabbitMQ. Файл consumer.py прослушивает очереди, добавляет логи в базу данных и отправляет сообщения о критических ошибках конкретному пользователю через Telegram.

# Технологии и инструменты:

Python (+ asyncio для асинхронной работы)

SQLAlchemy (ORM) + aiosqlite (асинхронная SQLite)

aiohttp (асинхронная библиотека для http-запросов к telegram)

pydantic (валидация данных)

pika и aio_pika (библиотеки для работы с RabbitMQ, pika - для producer'а, aio_pika - для consumer'а)
