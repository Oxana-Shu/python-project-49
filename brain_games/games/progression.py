from brain_games.games import engine
from brain_games.games import constants
from brain_games.games import get_random


def progression_game():
    engine.run_game(get_math_question_and_result,
                    constants.PROGRESSION_MESSAGE_START)


def get_math_question_and_result():
    PROGRESSION_LENGTH = get_random.get_random_number(5, 15)
    first_num = get_random.get_random_number(1, 15)
    diff = get_random.get_random_number(2, 10)
    missed_num_ind = get_random.get_random_number(0,PROGRESSION_LENGTH)
    progression = ' '.join([
        '..' if i == missed_num_ind else str(first_num + i * diff)
        for i in range(PROGRESSION_LENGTH)
    ])
    print(f'Question: {progression}')
    return first_num + missed_num_ind * diff
