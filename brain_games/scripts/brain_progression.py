#!/usr/bin/env python3

from brain_games.games import progression
from brain_games.games import logical


def main():
    print('Welcome to the Brain Games!')
    name = logical.welcome_user()
    progression.progression_game(name)


if __name__ == '__main__':
    main()
