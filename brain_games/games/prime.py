from brain_games.constants import PRIME_MESSAGE_START
from brain_games.engine import run_game
from brain_games.get_random import get_random_number


def get_math_question_and_result():
    num = get_random_number(1, 100)
    question = f'Question: {num}'
    return (question, 'yes') if is_prime(num) else (question, 'no')


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_game():
    run_game(get_math_question_and_result, PRIME_MESSAGE_START)
