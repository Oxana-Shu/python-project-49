from brain_games.games import logical
from brain_games.games import constants


def even_game():
    name = logical.welcome_user()
    print(constants.EVEN_MESSAGE_START)
    for i in range(logical.TRUE_ANSWERS_COUNT):
        num = create_example()
        answer = quest_and_answ(num)

        if is_even(num):
            even_detection('yes', answer, name)
            if answer != 'yes':
                return
            i += 1
        else:
            even_detection('no', answer, name)
            if answer != 'no':
                return
            i += 1

    logical.congratulations(name)


def is_even(num):
    return True if num % 2 == 0 else False


def even_detection(true_answer, answer, name):
    return logical.correct_answer() if (
        true_answer == answer
    ) else logical.wrong_answer(name, answer, true_answer)


def create_example():
    num = logical.get_random_number(1, 100)
    return num


def quest_and_answ(num):
    print(f'Question: {num}')
    return logical.user_answer()
