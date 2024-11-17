from brain_games.games import logical
from brain_games.games import constants


def calc_game():
    name = logical.welcome_user()
    print(constants.CALC_MESSAGE_START)
    for i in range(logical.TRUE_ANSWERS_COUNT):
        example = create_example()
        true_answer = example[1]
        user_answer = quest_and_answ(example[0])

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
        random_operation = logical.get_random_number(1, 3)
        match random_operation:
            case 1:
                example = (f'Question: {first_num} + {second_num}', first_num + second_num)
            case 2:
                example = (f'Question: {first_num} - {second_num}', first_num - second_num)
            case _:
                example = (f'Question: {first_num} * {second_num}', first_num * second_num)

        return example

def quest_and_answ(question):
    print(question)
    return logical.user_answer()
    

    


