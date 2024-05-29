from aiogram.types import InlineKeyboardButton

from bot.callback.user import UserActionCallback
from bot.keyboards.inline.main import Inline


class StartInlineButtonText:
    LEAVE_CONTACT = 'Хочу залишити контакти ☎️'
    SIGN_UP_FOR_VIEW = 'Хочу домовитись за перегляд 🔎'
    OTHER = 'Маю інші питання 💬'


leave_contact_button = InlineKeyboardButton(text=StartInlineButtonText.LEAVE_CONTACT,
                                            callback_data=UserActionCallback(LEAVE_CONTACT=1).pack(),
                                            )

sign_up_for_view_button = InlineKeyboardButton(text=StartInlineButtonText.SIGN_UP_FOR_VIEW,
                                               callback_data=UserActionCallback(SIGN_UP_FOR_VIEW=1).pack(),
                                               )
other_button = InlineKeyboardButton(text=StartInlineButtonText.OTHER,
                                    callback_data=UserActionCallback(OTHER_BUTTON=1).pack(),
                                    )

start_inline_markup = Inline([
    [leave_contact_button],
    [sign_up_for_view_button],
    [other_button],
])
