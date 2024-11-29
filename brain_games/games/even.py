from brain_games.engine import run_game
from brain_games.constants import EVEN_MESSAGE_START
from brain_games.get_random import get_random_number


def get_math_question_and_result():
    num = get_random_number(1, 100)
    quesion = f'Question: {num}'
    return (quesion, 'yes') if is_even(num) else (quesion, 'no')


def is_even(num):
    return num % 2 == 0


def even_game():
    run_game(get_math_question_and_result, EVEN_MESSAGE_START)
