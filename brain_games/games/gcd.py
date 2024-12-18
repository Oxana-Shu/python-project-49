from math import gcd

from brain_games.constants import GCD_MESSAGE_START
from brain_games.engine import run_game
from brain_games.get_random import get_random_number


def get_math_question_and_result():
    num1, num2 = (get_random_number(1, 100), get_random_number(1, 100))
    question = f'{num1} {num2}'
    return (question, gcd(num1, num2))


def gcd_game():
    run_game(get_math_question_and_result, GCD_MESSAGE_START)
