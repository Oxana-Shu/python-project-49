#!/usr/bin/env python3

from random import randint
from brain_games.games import logical

def calc_game(name):
    print('What is the result of the expression?')
    true_answers = 0
    while true_answers < logical.TRUE_ANSWERS_COUNT:
        random_number_first = randint (1,100)
        random_number_second = randint (1,100)
        random_operation = randint (1,3)
        match random_operation:
            case 1:
                operation = '+'
                true_answer = random_number_first + random_number_second
            case 2:
                operation = '-'
                true_answer = random_number_first - random_number_second
            case _:
                operation = '*'
                true_answer = random_number_first * random_number_second
        print (f'Question: {random_number_first} {operation} {random_number_second}')
        answer = logical.user_answer()
        if answer == str(true_answer):
            logical.correct_answer()
            true_answers += 1
        else:
            logical.wrong_answer(name,answer,true_answer)
            return
    
    logical.congatulations(name)