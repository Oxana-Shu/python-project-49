from brain_games.games import engine
from brain_games.games import constants


def progression_game():
    engine.run_game(get_math_question_and_result,
                    constants.PROGRESSION_MESSAGE_START)


def get_math_question_and_result():
    PROGRESSION_LENGTH = engine.get_random_number(5, 15)
    first_num = engine.get_random_number(1, 15)
    diff = engine.get_random_number(2, 10)
    missed_num_ind = engine.get_random_number(1, PROGRESSION_LENGTH)
    progression = ' '.join([
        '..' if i == missed_num_ind else str(first_num + i * diff)
        for i in range(PROGRESSION_LENGTH)
    ])
    print(f'Question: {progression}')
    return first_num + missed_num_ind * diff
