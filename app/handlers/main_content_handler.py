from aiogram.types import ContentTypes
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from database.db_manager import show_expired, unsub_list


class Content(StatesGroup):
    send_msg = State()

async def wait_message(message: types.Message, state: FSMContext):
    await message.answer("Enter the message for subscribers: ")
    await state.set_state(Content.send_msg.state)

async def send_message(message: types.Message, state: Content.send_msg):
    unsub, subbed = show_expired()
    for user_s in subbed:
        await message.bot.send_message(chat_id=user_s, text=message.text)

    unsub_list(unsub)
    for user_u in unsub:
        await message.bot.send_message(chat_id=user_u, text="Your subscription has expired. Please check [FIRST BOT] to update your subscription")


def register_handlers_content(dp: Dispatcher):
    dp.register_message_handler(wait_message, lambda msg: msg.text == "Send message", state="*")