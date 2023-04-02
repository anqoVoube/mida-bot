from typing import Tuple
from static import Static


import telebot
from telebot.types import Message


def with_expected_message(bot: telebot.TeleBot, message_expectations: Tuple[str]):
    def inner(func):
        def wrapper(message: Message):
            if message.text in message_expectations:
                func(message)
            else:
                received_message = bot.send_message(message.chat.id, Static.ERROR_MESSAGE)
                bot.register_next_step_handler(received_message, with_expected_message(bot, message_expectations)(func))

        return wrapper
    return inner
