from telebot import types


class Static:
    START = "start"
    HELP = "help"
    WELCOME_MESSAGE = "Привет! Я бот, который позволит тебе узнать чуть больше обо мне"
    TELL_ME_ABOUT_YOURSELF_TEXT = "Расскажи о себе"
    ERROR_MESSAGE = "Извините, что-то пошло не так. Пожалуйста попробуйте ещё раз"
    BIO_TEXT = """Меня зовут Jamoliddin. 
Основной стэк Python, но тем не менее присутствует небольшой опыт в разработке приложений с языками:

- Golang
- JavaScript
- Rust

Опыт работы как Back-End Developer (Python) больше одного года. За это время создал более чем 5 Telegram ботов разных сложностей.

Ссылки для более подробной информации о проделанных работах и скиллах

- LinkedIn: https://www.linkedin.com/in/jamoliddin-bakhriddinov/
- GitHub: github.com/anqovoube
"""
    CASES_TEXT = "Кейсы"

    FIRST_PROJECT = """Недавно созданный бот. Написан на telethon. Его работой являются:

- Рассылать группам сообщение каждый промежуток времени, указанным админом (к примеру каждый час) 
- Получать команды с админа (редактировать время и группы, добавлять, удалять)

Проблема решена через чистую асинхронку. Настроен и стоит в продакшене

Source: https://github.com/anqoVoube/showcase
"""
    SECOND_PROJECT = """Бот, который Вы сейчас используете. Написан на pyTelegramBotAPI.

Source: https://github.com/anqoVoube/mida-bot

"""
    THIRD_PROJECT = """Бот, который работает с системой жертвы. Написан на pyTelegramBotAPI. Его работой являются:

- Получать команды с создателя (только он имеет доступ)
- Получать полный контроль над компьютером, при запуске exe файла.

Source: Проект удалён полностью, чтобы другие им не злоупотребляли, т.к он был создан исключительно в познавательных целях.
"""

    FOURTH_PROJECT = """Интеграция CRM и бота. Бот работает как crontab. Написан на pyTelegramBotAPI с DjangoRestFramework. Его работой являются:

- Получать и отправлять сведения о сегодняшне проделанной работе каждого сотрудника и их статистика.

Source: Код конфиденциальный.
"""
    END_TEXT = "На этом всё!"
    INFO_TEXT = "@youngerwolf"

    @staticmethod
    def get_default_reply_keyboard_markup() -> types.ReplyKeyboardMarkup:
        return types.ReplyKeyboardMarkup(True, True)
