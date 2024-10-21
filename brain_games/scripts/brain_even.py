#!/usr/bin/env python3

from brain_games.games import even
from brain_games.games import logical


def main():
    print('Welcome to the Brain Games!')
    name = logical.welcome_user()
    even.even_game(name)


if __name__ == '__main__':
    main()
