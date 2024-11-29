from brain_games.constants import PROGRESSION_MESSAGE_START
from brain_games.engine import run_game
from brain_games.get_random import get_random_number


def get_math_question_and_result():
    length_progression = get_random_number(5, 5)
    start_progression = get_random_number(1, 15)
    diff = get_random_number(2, 10)
    missed_num_ind = get_random_number(0, length_progression - 1)
    progression = ' '.join([
        '..' if i == missed_num_ind else str(start_progression + i * diff)
        for i in range(length_progression)
    ])
    question = f'Question: {progression}'
    return (question, start_progression + missed_num_ind * diff)


def progression_game():
    run_game(
        get_math_question_and_result, PROGRESSION_MESSAGE_START
    )
