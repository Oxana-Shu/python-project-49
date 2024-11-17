from brain_games.games import logical
from brain_games.games import constants


def prime_game():
    name = logical.welcome_user()
    print(constants.PRIME_MESSAGE_START)
    for i in range(constants.TRUE_ANSWERS_COUNT):
        num = create_example()
        user_answer = quest_and_answ(num)
        true_answer = is_prime(num)
        user_is_true = is_user_unswer(user_answer, true_answer)
        if user_is_true:
            logical.correct_answer()
            i += 1
        else:
            true_answer = 'yes' if true_answer else 'no'
            logical.wrong_answer(name, user_answer, true_answer)
            return
    logical.congratulations(name)


def create_example():
    num = logical.get_random_number(1, 100)
    return num


def quest_and_answ(num):
    print(f'Question: {num}')
    return logical.user_answer()


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def is_user_unswer(user_answer, true_answer):
    return True if (
        user_answer == 'yes'
        and true_answer
    ) or (user_answer == 'no' and not true_answer) else False
