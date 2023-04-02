from typing import Tuple

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

META = "Meta"


class EventFactory(type):
    """
    Этот Metaclass можно улучшить и сделать более гибким, но я не стал, чтобы не усложнять.

    """
    def __new__(mcls, name, bases, attrs):
        if meta_class := attrs.get(META):
            try:
                fields: Tuple[Tuple[Tuple[str, dict]]] = meta_class.fields
            except AttributeError as exc:
                raise AttributeError("Meta Class should have `fields`") from exc

            if fields:
                new_attrs = {}
                for raw_count, (text, keyboard) in enumerate(fields, start=1):
                    markup = InlineKeyboardMarkup()
                    for keyboard_count, row in enumerate(keyboard, start=1):
                        markup.add(*(InlineKeyboardButton(keyboard_text, **kwargs, callback_data=f"{raw_count}_{keyboard_count}") for keyboard_text, kwargs in row))
                    new_attrs[f"event{raw_count}"] = (text, markup)

                def initial(self):
                    return self.event1

                class_ = super().__new__(mcls, name, bases, new_attrs)
                setattr(class_, initial.__name__, initial)
                return class_

            raise AttributeError("`fields` is required to be populated with something...")

        raise KeyError("Your class should have inner class `Meta`")


class BaseKeyboardHandler:
    def initial(self):
        pass
