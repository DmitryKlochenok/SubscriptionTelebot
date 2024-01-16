from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext



async def cmd_start(message: types.Message, state: FSMContext):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    card_button = types.KeyboardButton("Card")
    crypto_button = types.KeyboardButton("Crypto")
    markup.add(card_button, crypto_button)

    await message.answer(text=f"""
Welcome to the bot! 

Choose the preferable payment system to continue""", reply_markup=markup)


async def cmd_terms(message: types.Message, state: FSMContext):
    await message.answer("After purchasing the subscription you will get the access to the bot with tips for a month. After a month passes you will be automatically unsubscribed and notified that the subscription is over. If you pay for the subscription before the period passes, the period will be extended.")


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_terms, commands="terms", state="*")
