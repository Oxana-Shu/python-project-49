import prompt

from brain_games.constants import COUNTS_ROUND


def run_game(get_math_question_and_result, game_instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{game_instruction}')

    for _ in range(COUNTS_ROUND):
        question, answer = get_math_question_and_result()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
