#!/usr/bin/env python3

from random import randint
from brain_games.games import logical


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    true_answers = 0
    while true_answers < logical.TRUE_ANSWERS_COUNT:
        random_number = randint (1,100)
        print(f'Question: {random_number}')
        answer = logical.user_answer()
        if random_number % 2 == 0: 
            if answer == 'yes':
                logical.correct_answer()
                true_answers += 1
            else:
                true_answer = 'yes'
                logical.wrong_answer(name,answer,true_answer)
                return
        else: 
            if answer == 'no':
                logical.correct_answer()
                true_answers += 1
            else:
                true_answer = 'no'
                logical.wrong_answer(name,answer,true_answer)
                return
                
    logical.congatulations(name)