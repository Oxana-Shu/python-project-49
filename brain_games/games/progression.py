from brain_games.games import logical
from brain_games.games import constants


def progression_game():
    name = logical.welcome_user()
    print(constants.PROGRESSION_MESSAGE_START)
    for i in range(constants.TRUE_ANSWERS_COUNT):
        length_progression = logical.get_random_number(5, 15)
        start_progression = logical.get_random_number(1, 15)
        step_progression = logical.get_random_number(2, 10)
        miss_position = logical.get_random_number(1, length_progression)
        create_example(length_progression, start_progression, step_progression, miss_position)
        true_answer = start_progression + miss_position * step_progression
        answer = logical.user_answer()
        if answer == str(true_answer):
            logical.correct_answer()
            i += 1
        else:
            logical.wrong_answer(name, answer, true_answer)
            return
    logical.congratulations(name)

def create_example(length, start, step, miss):
    question = 'Question:'
    for k in range(1, length + 1):
        if k != miss:
            question += ' ' + str(start + k * step)
        else:
            question += ' ..'
    print(question)


