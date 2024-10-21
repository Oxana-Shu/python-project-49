#!/usr/bin/env python3

from random import randint
from brain_games.games import logical


def gcd_game(name):
    print('Find the greatest common divisor of given numbers.')
    true_answers = 0
    while true_answers < logical.TRUE_ANSWERS_COUNT:
        random_number_first = randint (1,100)
        random_number_second = randint (1,100)
        true_answer = gcd(random_number_first,random_number_second)
        print(f'Question: {random_number_first} {random_number_second}')
        answer = logical.user_answer()
        if answer == str(true_answer):
            logical.correct_answer()
            true_answers += 1
        else:
            logical.wrong_answer(name,answer,true_answer)
            return
    logical.conrgatulations(name)

def gcd(first_number,second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    return first_number + second_number
