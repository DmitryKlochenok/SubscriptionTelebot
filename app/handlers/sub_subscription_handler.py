from aiogram.types import ContentTypes
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from app.config import PROVIDER_TOKEN, sub_price_card, currency_card
from database.db_manager import add_user
import time

class Subscription_card(StatesGroup):
    sub_pre_checkout = State()
    sub_successful_pay = State()
    create_subscription = State()

class Subscription_crypto(StatesGroup):
    pass


async def invoice_card(message: types.Message, state: FSMContext):
    prices = [types.LabeledPrice(label='Card Subscription', amount=sub_price_card)]
    await message.bot.send_invoice(
        message.chat.id,  # chat_id
        title='Subscription',  # title
        description=f'Monthly subscription to the tips bot',  # description
        provider_token=PROVIDER_TOKEN,  # provider_token
        currency=currency_card,  # currency
        is_flexible=False,  # True If you need to set up Shipping Fee
        prices=prices,  # prices
        start_parameter='sub_bought',
        payload='sub_payload')  # invoice_payload
    await state.set_state(Subscription_card.sub_pre_checkout.state)


async def sub_successful_payment(pre_checkout_query: types.PreCheckoutQuery, state: Subscription_card.sub_pre_checkout):
    await pre_checkout_query.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                        error_message="Error! Please try again or message the creator of this bot if the error hasn't disappeared")
    await Subscription_card.create_subscription.set()



async def invoice_crypto(message: types.Message, state: FSMContext):
    pass




async def create_subscription(message: types.Message, state: Subscription_card.create_subscription):
    await message.answer("Thanks for your order! You can now start @[MAIN BOT] to start receiving tips")
    add_user(message.from_user.id, round(time.time()+2592000))


def register_handlers_subscription(dp: Dispatcher):
    dp.register_message_handler(invoice_card, lambda msg: msg.text == "Card", state="*")
    dp.register_pre_checkout_query_handler(sub_successful_payment, lambda query: True, state=Subscription_card.sub_pre_checkout)
    dp.register_message_handler(invoice_crypto, lambda msg: msg.text == "Crypto", state="*")

