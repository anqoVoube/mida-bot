import os
from typing import Tuple

import telebot
from dotenv import load_dotenv
from telebot.types import Message

from static import Static
from utils import with_expected_message
from utils.factory import EventFactory, BaseKeyboardHandler


load_dotenv()

TOKEN = os.environ.get("TOKEN")
CONTACTS = os.environ.get("CONTACTS")

bot = telebot.TeleBot(TOKEN)


class NextInlineKeyboardHandler(BaseKeyboardHandler, metaclass=EventFactory):
    class Meta:
        """
        (
            (
                ("Предыдущий", {}),
                ("Cледующий", {}),
            ),
            (
                ("Левый", {}),
                ("Правый", {}),
            )
        ) -> Buttons UI, where {} is extra kwargs

            |Предыдущий||Следующий|
            |  Левый  || Правый |

        """
        fields: Tuple[Tuple[str, dict]] = (
            (Static.FIRST_PROJECT, ((("Cледующий", {}),),)),
            (Static.SECOND_PROJECT, ((("Cледующий", {}),),)),
            (Static.THIRD_PROJECT, ((("Cледующий", {}),),)),
            (Static.FOURTH_PROJECT, ((("Cледующий", {}),),)),
            (Static.END_TEXT, ((("Контакты", {"url": CONTACTS}),),)),
        )


generated_events = NextInlineKeyboardHandler()


@bot.message_handler(commands=[Static.START, Static.HELP])
def send_welcome(message: Message):
    source_language_menu = Static.get_default_reply_keyboard_markup()
    source_language_menu.row(Static.TELL_ME_ABOUT_YOURSELF_TEXT)
    received_message = bot.send_message(message.chat.id, Static.WELCOME_MESSAGE, reply_markup=source_language_menu)
    bot.register_next_step_handler(received_message, bio_handler)


@with_expected_message(bot, (Static.TELL_ME_ABOUT_YOURSELF_TEXT,))
def bio_handler(message: Message):
    cases = Static.get_default_reply_keyboard_markup()
    cases.row(Static.CASES_TEXT)
    received_message = bot.send_message(message.chat.id, Static.BIO_TEXT, reply_markup=cases)
    bot.register_next_step_handler(received_message, cases_handler)


@with_expected_message(bot, (Static.CASES_TEXT,))
def cases_handler(message):
    text, markup = generated_events.initial()
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # I didn't make it too complicated, since requirements say to implement only Next (Следующий) logic case
    event_number, _ = map(int, call.data.split("_"))
    text, markup = getattr(generated_events, f"event{event_number + 1}")
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=text, reply_markup=markup)


bot.polling()


