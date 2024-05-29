from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from sqlalchemy import select

from bot.callback.user import UserActionCallback
from bot.config import MessageText
from bot.database.main import SessionLocal
from bot.database.models.user import User
from bot.fsm.contact import DialogState, SignupForViewState, OtherState
from bot.handlers.user.start import start_handler
from bot.misc.util import send_message_to_admins

contact_router = Router()


class DialogText:
    questions = {
        1: 'Як давно ви в Англії ?',
        2: 'В якому місті проживаєте зараз?',
        3: 'Знімаєте кімнату або живете у спонсорів?',
        4: 'Коли потрібно переїхати?',
        5: 'Який район розглядаєте для проживання?',
        6: 'Хто буде проживати?',
        7: 'На яку суму розраховуєте?',
        8: 'Звідки про нас дізнались?',
    }


@contact_router.callback_query(UserActionCallback.filter(F.LEAVE_CONTACT == 1))
async def leave_contact_handler(query: CallbackQuery, state: FSMContext):
    await query.message.answer(text=MessageText.LEAVE_CONTACT)
    await query.message.answer(text=DialogText.questions[1])
    await state.set_state(DialogState.answering)
    await state.update_data({'question': 1})
    await query.answer()


@contact_router.message(StateFilter(DialogState.answering), F.text)
async def answer_to_question_handler(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    question_number = data['question']
    next_question_number = question_number + 1
    data.update({
        'question': next_question_number,
        f'{question_number}_message_answer': message.text,
    })
    if not DialogText.questions.get(next_question_number):
        questions_and_answers = ''.join([MessageText.QUESTION_ANSWER.format(
            question=DialogText.questions[int(key[0])],
            answer=data[key],
        )
            for key in data.keys() if key[0].isnumeric()])

        answers_outcomes = MessageText.QUESTION_OUTCOMES.format(
            telegram_id=message.from_user.id,
            username=message.from_user.username or message.from_user.first_name,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name or MessageText.NOT_SET,
            questions_and_answers=questions_and_answers,
        )
        await message.answer(text=MessageText.LEAVE_CONTACT_SUCCESSFUL)
        await start_handler(message)
        await send_message_to_admins(
            answers_outcomes,
            bot,
        )
        await state.clear()
        return

    await message.answer(text=DialogText.questions[next_question_number])
    await state.set_data(data)


@contact_router.callback_query(UserActionCallback.filter(F.SIGN_UP_FOR_VIEW == 1))
async def sign_up_for_view_handler(query: CallbackQuery, state: FSMContext):
    await query.message.answer(text=MessageText.SIGN_UP_FOR_VIEW)
    await state.set_state(SignupForViewState.answering)
    await query.answer()


@contact_router.message(StateFilter(SignupForViewState.answering), F.text)
async def sign_up_for_view_successful_handler(message: Message, bot: Bot, state: FSMContext):
    await send_message_to_admins(MessageText.SIGN_UP_FOR_VIEW_SUCCESSFUL.format(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name or MessageText.NOT_SET,
        message=message.text,
    ), bot)
    await message.answer(text=MessageText.MESSAGE_SUCCESSFUL)
    await start_handler(message)
    await state.clear()


@contact_router.callback_query(UserActionCallback.filter(F.OTHER_BUTTON == 1))
async def other_button_handler(query: CallbackQuery, state: FSMContext):
    await query.message.answer(text=MessageText.OTHER_BUTTON)
    await state.set_state(OtherState.answering)
    await query.answer()


@contact_router.message(StateFilter(OtherState.answering), F.text)
async def other_button_successful_handler(message: Message, bot: Bot, state: FSMContext):
    await send_message_to_admins(MessageText.OTHER_BUTTON_SUCCESSFUL.format(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name or MessageText.NOT_SET,
        message=message.text,
    ), bot)
    async with SessionLocal.begin() as session:
        query = select(User.username).filter_by(is_admin=True)
        statement = await session.execute(query)
        admins_username = statement.scalars()

    await message.answer(text=MessageText.ADMIN_LIST.format(contacts=', '.join([f'@{username}' for username in admins_username])))
    await message.answer(text=MessageText.MESSAGE_SUCCESSFUL)
    await start_handler(message)
    await state.clear()
