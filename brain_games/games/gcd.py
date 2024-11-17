from brain_games.games import logical
from brain_games.games import constants
from math import gcd


def gcd_game():
    name = logical.welcome_user()
    print(constants.GCD_MESSAGE_START)
    for i in range(logical.TRUE_ANSWERS_COUNT):
        example = create_example()
        user_answer = quest_and_answ(example[0])
        true_answer = example[1]
        if user_answer == str(true_answer):
            logical.correct_answer()
            i += 1
        else:
            logical.wrong_answer(name, user_answer, true_answer)
            return
    logical.congratulations(name)


def create_example():
    first_num = logical.get_random_number(1, 100)
    second_num = logical.get_random_number(1, 100)
    example = (
        f'Question: {first_num} {second_num}',
        gcd(first_num, second_num)
    )
    return example


def quest_and_answ(question):
    print(question)
    return logical.user_answer()
