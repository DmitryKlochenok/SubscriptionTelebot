from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from app.config import whitelist


async def cmd_start(message: types.Message, state: FSMContext):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if message.from_user.id in whitelist:
        msg_button = types.KeyboardButton("Send message")
        markup.add(msg_button)

    await message.answer(text=f"""
Welcome to the bot! 

Here you will get the tips if subscribed""", reply_markup=markup)



def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")