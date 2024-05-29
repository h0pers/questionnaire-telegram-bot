from aiogram.fsm.state import StatesGroup, State


class DialogState(StatesGroup):
    answering = State()


class SignupForViewState(StatesGroup):
    answering = State()


class OtherState(StatesGroup):
    answering = State()
