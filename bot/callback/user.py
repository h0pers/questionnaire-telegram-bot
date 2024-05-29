from aiogram.filters.callback_data import CallbackData


class UserActionCallback(CallbackData, prefix="user"):
    LEAVE_CONTACT: int = 0
    SIGN_UP_FOR_VIEW: int = 0
    OTHER_BUTTON: int = 0
