#!/usr/bin/env python3

import prompt


TRUE_ANSWERS_COUNT = 3


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer


def correct_answer():
    print('Correct!')


def wrong_answer(name, answer, true_answer):
    print(f''''{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.
Let's try again, {name}!''')


def congratulations(name):
    print(f'Congratulations, {name}!')
