import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))

DB_URL = conn_url = f'postgresql+asyncpg://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST")}/{os.getenv("POSTGRES_DB")}'

BOT_TOKEN = os.getenv('BOT_TOKEN')

REDIS_PORT = os.getenv('REDIS_PORT')

REDIS_HOST = os.getenv('REDIS_HOST')


class MessageText:
    LEAVE_CONTACT = 'Вітаю! Мене звати бот <b>Rent House.</b> Дозволь поставити декілька питань, так я швидше зрозумію як тобі допомогти.'
    WELCOME = 'Вітаю! Мене звати бот <b>Rent House.</b>'
    LEAVE_CONTACT_SUCCESSFUL = 'Дякуємо за ваші відповіді, залиште ваші контакти, щоб наш менеджер звʼязався з вами. А поки ви очікуєте, підписуйтесь на наші соціальні мережі, де ви зможете подивитись відгуки від клієнтів.'
    MESSAGE_SUCCESSFUL = 'Дякуємо за вашу відповідь, а поки ви очікуєте, підписуйтесь на наші соціальні мережі, де ви зможете подивитись відгуки від клієнтів.'
    QUESTION_OUTCOMES = '''
<b>✍️ КОРИСТУВАЧ ЗАЛИШИВ КОНТАКТ ✍️</b>

<b>ID Користувача</b>: <code>{telegram_id}</code>
<b>Користувач</b>: @{username}
<b>Ім'я</b>: <code>{first_name}</code>
<b>Фамілія</b>: <code>{last_name}</code>
{questions_and_answers}
'''
    QUESTION_ANSWER = '''
<b>Питання:</b> {question}
<b>Відповідь</b> {answer}
'''

    NOT_SET = 'Не встановлено'
    SIGN_UP_FOR_VIEW = 'Напишіть ваш номер телефону, та яка пропозиція зацікавила, менеджер зателефонує та назначить день та час для перегляду.'
    SIGN_UP_FOR_VIEW_SUCCESSFUL = '''
<b>🔎 КОРИСТУВАЧ БАЖАЄ ДОМОВИТИСЯ ЗА ПЕРЕГЛЯД 🔎</b>
<b>ID Користувача</b>: <code>{telegram_id}</code>
<b>Користувач</b>: @{username}
<b>Ім'я</b>: <code>{first_name}</code>
<b>Фамілія</b>: <code>{last_name}</code>
<b>Повідомлення</b>: 
<i>{message}</i>
'''
    OTHER_BUTTON = 'Привіт, задайте ваші питання і наш менеджер вам відповість.'
    OTHER_BUTTON_SUCCESSFUL = '''
<b>🔎 КОРИСТУВАЧ МАЄ ІНШЕ ПИТАННЯ 🔎</b>
<b>ID Користувача</b>: <code>{telegram_id}</code>
<b>Користувач</b>: @{username}
<b>Ім'я</b>: <code>{first_name}</code>
<b>Фамілія</b>: <code>{last_name}</code>
<b>Повідомлення</b>: 
<i>{message}</i>
'''
    ADMIN_LIST = 'Контакти менеджера: {contacts}'
