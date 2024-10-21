#!/usr/bin/env python3

from random import randint
from brain_games.games import logical


def prime_game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    true_answers = 0
    while true_answers < logical.TRUE_ANSWERS_COUNT:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = logical.user_answer()
        true_answer = check_for_prime(random_number)
        if answer == true_answer:
            logical.correct_answer()
            true_answers += 1
        else:
            logical.wrong_answer(name, answer, true_answer)
            return
    logical.congratulations(name)


def check_for_prime(number):
    if number <= 1:
        return 'no'
    if number == 2:
        return 'yes'
    if number % 2 == 0:
        return 'no'
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return 'no'
    return 'yes'
