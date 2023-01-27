import json
import random
from typing import List, Dict, Any
from inspect import cleandoc as clean_msg

from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

router = Router()
questions_file_path = 'resources/test_questions.json'


class Test(StatesGroup):
    test_in_progress = State()


async def send_question(message: types.Message, questions_order: List[int], number: int) -> types.Message:
    with open(questions_file_path) as f:
        question = json.load(f)[questions_order[number]]
    options = question['options']
    options_order = random.sample(tuple(range(len(options))), len(options))
    return await message.answer_poll(
        type="quiz",
        question=f"[{number + 1}/{len(questions_order)}]{question['question']}",
        options=[options[i] for i in options_order],
        correct_option_id=options_order.index(question['correct_option']),
        explanation=question.get('explanation'),
        is_anonymous=False
    )


@router.message(Command("test"))
async def cmd_test(message: types.Message, state: FSMContext) -> None:
    with open(questions_file_path) as f:
        questions_count = len(json.load(f))
    await state.set_state(Test.test_in_progress)
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


@router.poll_answer(Test.test_in_progress)
async def handle_poll_answer(answer: types.PollAnswer, state: FSMContext) -> None:
    state_data: Dict[str, Any] = await state.get_data()
    message: types.Message = state_data['poll_message']
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
        await message.answer(clean_msg(
            f"""
            📙 <b>Тест закончен</b>
            <b>Твой результат:</b> {correct_answers}/{questions_count}
            """
        ))
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
