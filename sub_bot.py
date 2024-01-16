
import asyncio
import time

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from app.config import TOKEN_SUB
from app.handlers.sub_common_handler import register_handlers_common
from app.handlers.sub_subscription_handler import register_handlers_subscription
from database.db_manager import show_expired, unsub_list


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start"),
        BotCommand(command="/terms", description="Terms")
    ]
    await bot.set_my_commands(commands)

async def main_sub():
    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=TOKEN_SUB)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Регистрация хэндлеров
    register_handlers_common(dp)
    register_handlers_subscription(dp)

    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    # await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await dp.start_polling()


