
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from app.config import TOKEN_MAIN
from app.handlers.main_common_handler import register_handlers_common
from app.handlers.main_content_handler import register_handlers_content


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start"),
    ]
    await bot.set_my_commands(commands)

async def main_main():
    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=TOKEN_MAIN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Регистрация хэндлеров
    register_handlers_common(dp)
    register_handlers_content(dp)

    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    # await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await dp.start_polling()

