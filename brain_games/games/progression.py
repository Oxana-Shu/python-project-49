#!/usr/bin/env python3

from random import randint
from brain_games.games import logical


def progression_game(name):
    print('What number is missing in the progression?')
    true_answers = 0
    while true_answers < logical.TRUE_ANSWERS_COUNT:
        length_progression = randint(5, 15)
        start_progression = randint(1, 15)
        step_progression = randint(2, 10)
        miss_position = randint(1, length_progression)
        question = 'Question:'
        for k in range(1, length_progression + 1):
            if k != miss_position:
                question += ' ' + str(start_progression + k * step_progression)
            else:
                question += ' ..'
                true_answer = start_progression + k * step_progression
        print(question)
        answer = logical.user_answer()
        if answer == str(true_answer):
            logical.correct_answer()
            true_answers += 1
        else:
            logical.wrong_answer(name, answer, true_answer)
            return
    logical.congratulations(name)
