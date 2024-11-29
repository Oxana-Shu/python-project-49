from random import choice

from brain_games.constants import CALC_MESSAGE_START
from brain_games.engine import run_game
from brain_games.get_random import get_random_number


def get_math_question_and_result():
    num1 = get_random_number(1, 100)
    num2 = get_random_number(1, 100)
    operation, right_answer = get_random_operation(num1, num2)
    question = f'Question: {num1} {operation} {num2}'
    return (question, right_answer)


def get_random_operation(num1, num2):
    operations = [
        ('+', num1 + num2),
        ('-', num1 - num2),
        ('*', num1 * num2),
    ]
    return choice(operations)


def calc_game():
    run_game(get_math_question_and_result, CALC_MESSAGE_START)
