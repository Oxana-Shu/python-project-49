import prompt
from random import randint
from brain_games.games import constants


def user_interaction(context, name=None, answer=None, right_answer=None):
    match context:
        case 'welcome':
            name = prompt.string(
                '''Welcome to the Brain Games!\nMay I have your name? '''
            )
            print(f'Hello, {name}!')
            return name
        case 'answer':
            answer = prompt.string('Your answer: ')
            return answer
        case 'correct':
            print('Correct!')
        case 'wrong':
            print(
                f"{answer} is wrong answer ;(."
                f" Correct answer was {right_answer}."
                f" Let's try again, {name}!"
            )
        case 'congratulations':
            print(f'Congratulations, {name}!')


def get_random_number(start, end):
    return randint(start, end)


def run_game(get_math_question_and_result, CALC_INSTRUCTION):
    name = user_interaction('welcome')
    print(CALC_INSTRUCTION)
    for i in range(constants.COUNTS_ROUND):
        right_answer = get_math_question_and_result()
        user_answer = user_interaction('answer')
        if user_answer == str(right_answer):
            user_interaction('correct')
            i += 1
        else:
            user_interaction('wrong', name, user_answer, right_answer)
            return
    user_interaction('congratulations', name=name)
