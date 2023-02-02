import json
import random
from typing import List, Dict, Any
from inspect import cleandoc as clean_msg

from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards import main_menu_keyboard

router = Router()
questions_file_path = 'resources/quiz_questions.json'


class Quiz(StatesGroup):
    quiz_in_progress = State()


async def send_question(message: types.Message, questions_order: List[int], number: int) -> types.Message:
    with open(questions_file_path) as f:
        question = json.load(f)[questions_order[number]]
    options = question['options']
    options_order = random.sample(tuple(range(len(options))), len(options))
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="❌ Прервать тест")]],
        resize_keyboard=True
    )
    return await message.answer_poll(
        type="quiz",
        question=f"[{number + 1}/{len(questions_order)}] {question['question']}",
        options=[options[i] for i in options_order],
        correct_option_id=options_order.index(question['correct_option'] - 1),
        explanation=question.get('explanation'),
        is_anonymous=False,
        reply_markup=keyboard
    )


async def send_results(
    message: types.Message,
    title: str,
    correct_answers: int,
    questions_passed: int,
) -> types.Message:
    if questions_passed < 5:
        comment = "Рекомендуем пройти тест ещё раз и проверить свои знания."
    else:
        percentage = correct_answers / questions_passed
        if percentage <= 0.2:
            comment = clean_msg(
                """
                Тебе предстоит ещё многое узнать о правилах этикета.
                Подпишись на наш <a href="https://t.me/cultural_code_lyceum">канал</a> и откроешь для себя много нового.
                """
            )
        elif percentage <= 0.5:
            comment = clean_msg(
                """
                Ты знаешь базовые правила этикета, молодец. Но никогда не помешает знать чуть больше.
                Подпишись на наш <a href="https://t.me/cultural_code_lyceum">канал</a>, чтобы улучшить свой результат. 
                """
            )
        elif percentage <= 0.8:
            comment = clean_msg(
                """
                Ты, вероятно, знаешь уже многое о культуре и правилах этикета, но совершенствоваться всегда полезно.
                В нашем <a href="https://t.me/cultural_code_lyceum">канале</a> ты сможешь узнать ещё больше.
                """
            )
        else:
            comment = clean_msg(
                """
                Ты знаешь всё об этикете. Достойно уважения. Но нет предела совершенству.
                В нашем <a href="https://t.me/cultural_code_lyceum">канале</a> мы регулярно рассказываем что-то интересное.
                """
            )
    main_text = clean_msg(
        f"""
        📙 <b>{title}</b>
        <b>Твой результат:</b> {correct_answers}/{questions_passed}
        """
    )
    return await message.answer(
        text=f"{main_text}\n{comment}",
        reply_markup=main_menu_keyboard
    )


@router.message(Command("quiz", "test"), State())
@router.message(Text("📙 Пройти тест"), State())
async def cmd_quiz(message: types.Message, state: FSMContext) -> None:
    with open(questions_file_path) as f:
        questions_count = len(json.load(f))
    await state.set_state(Quiz.quiz_in_progress)
    questions_order = random.sample(tuple(range(questions_count)), questions_count)
    poll = await send_question(
        message=message,
        questions_order=questions_order,
        number=0
    )
    await state.update_data(
        poll_message=poll,
        question_number=0,
        questions_order=questions_order,
        correct_answers=0
    )


@router.message(Command("cancel"), Quiz.quiz_in_progress)
@router.message(Text("❌ Прервать тест"), Quiz.quiz_in_progress)
async def cmd_cancel(message: types.Message, state: FSMContext) -> None:
    state_data = await state.get_data()
    correct_answers: int = state_data['correct_answers']
    questions_passed = state_data['question_number'] + 1
    await state.clear()
    await send_results(
        message=message,
        title="Тест прерван",
        correct_answers=correct_answers,
        questions_passed=questions_passed
    )


@router.poll_answer(Quiz.quiz_in_progress)
async def handle_poll_answer(answer: types.PollAnswer, state: FSMContext) -> None:
    state_data: Dict[str, Any] = await state.get_data()
    message: types.Message = state_data['poll_message']
    if answer.poll_id != message.poll.id:
        return
    correct_answers: int = state_data['correct_answers']
    question_number: int = state_data['question_number'] + 1
    questions_count = len(state_data['questions_order'])
    if answer.option_ids[0] == message.poll.correct_option_id:
        correct_answers += 1
        await message.answer("✅ Правильно! Молодец!")
    else:
        await message.answer("❌ Неправильно! В следующий раз всё получится!")
    if question_number == questions_count:
        await state.clear()
        await send_results(
            message=message,
            title="Тест пройден",
            correct_answers=correct_answers,
            questions_passed=questions_count
        )
    else:
        poll = await send_question(
            message=message,
            questions_order=state_data['questions_order'],
            number=question_number
        )
        await state.update_data(
            poll_message=poll,
            question_number=question_number,
            correct_answers=correct_answers
        )
