from brain_games.games import engine
from brain_games.games import constants


def prime_game():
    engine.run_game(get_math_question_and_result, constants.PRIME_MESSAGE_START)


def get_math_question_and_result():
    num = engine.get_random_number(1, 100)
    print(f'Question: {num}')
    return 'yes' if is_prime(num) else 'no'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
