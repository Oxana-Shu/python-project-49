#!/usr/bin/env python3

import prompt
from random import randint

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def parity_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    true_answers = 0
    while true_answers < 3:
        random_number = randint (1,100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0: 
            if answer == 'yes':
                print ('Correct!')
                true_answers += 1
            else:
                print(f''' '{answer}' is wrong answer ;(. Correct answer was 'yes'.
                      Let's try again, {name}!''')
                return
        else: 
            if answer == 'no':
                print ('Correct!')
                true_answers += 1
            else:
                print(f''' '{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!''')
                return
                
    print(f'Congratulations, {name}!')