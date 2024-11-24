from brain_games.games import engine
from brain_games.games import constants
from math import gcd


def gcd_game():
    engine.run_game(get_math_question_and_result, constants.GCD_MESSAGE_START)


def get_math_question_and_result():
    first_num = engine.get_random_number(1, 100)
    second_num = engine.get_random_number(1, 100)
    print(f'Question: {first_num} {second_num}')
    return gcd(first_num, second_num)
