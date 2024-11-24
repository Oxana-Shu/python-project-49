from brain_games.games import engine
from brain_games.games import constants
from brain_games.games import get_random
import random


def calc_game():
    engine.run_game(get_math_question_and_result, constants.CALC_MESSAGE_START)


def get_math_question_and_result():
    first_num = get_random.get_random_number(1, 100)
    second_num = get_random.get_random_number(1, 100)
    choises = [
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num),
    ]
    operation, right_answer = random.choice(choises)
    print(f'Question: {first_num} {operation} {second_num}')
    return right_answer
