from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from app.config import whitelist
from database.db_manager import show_expired, get_unsub_date


async def cmd_start(message: types.Message, state: FSMContext):
    unsub_date = get_unsub_date(message.from_user.id)
    unsub, subbed = show_expired()
    if message.from_user.id in whitelist:
        await message.answer("""Hello admin!

Write any message you want to share with your subscribers:""")
    elif message.from_user.id in unsub:
        await message.answer("""Hello! 

You are not subscribed to this service 

You can get the subscription in @[FIRST BOT]""")
    elif message.from_user.id in subbed:
        await message.answer(f"""Hello!
        
Your subscription is active till {unsub_date}

Enjoy the service!""")

    else:
        await message.answer("""Hello! 

You are not subscribed to this service 

You can get the subscription in @[FIRST BOT]""")


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")