#!/usr/bin/env python
import json
import aio_pika
import aio_pika.abc
from telegram_sender import TelegramSender
from repositories.note_repository import NoteRepository
from config.init_db import init_db
from config.database import get_db
import asyncio


async def on_message_green(message: aio_pika.abc.AbstractIncomingMessage):
    async with message.process():
        mes = json.loads(message.body.decode("utf-8"))
        async for db in get_db():
            note_rep = NoteRepository(db)
            await note_rep.create(mes)
            print("Green it is good, don't worry!")


async def on_message_red(message: aio_pika.abc.AbstractIncomingMessage):
    async with message.process():
        mes = json.loads(message.body.decode("utf-8"))
        print("Oh, red")
        async for db in get_db():
            note_rep = NoteRepository(db)
            await note_rep.create(mes)
            tg_sender = TelegramSender()
            await tg_sender.send_message(f" [x] ALERT from red: {mes}")


async def consume_queue(
    channel: aio_pika.abc.AbstractChannel, queue_name: str, process_message_func
):
    queue = await channel.declare_queue(queue_name)
    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            await process_message_func(message)


async def main(loop):
    await init_db()
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/", loop=loop
    )
    async with connection:
        channel = await connection.channel()
        await asyncio.gather(
            consume_queue(channel, "green", on_message_green),
            consume_queue(channel, "red", on_message_red),
        )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
