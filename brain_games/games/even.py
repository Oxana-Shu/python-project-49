from brain_games.games import engine
from brain_games.games import constants


def even_game():
    engine.run_game(get_math_question_and_result, constants.EVEN_MESSAGE_START)


def get_math_question_and_result():
    num = engine.get_random_number(1, 100)
    print(f'Question: {num}')
    return 'yes' if is_even(num) else 'no'


def is_even(num):
    return True if num % 2 == 0 else False
