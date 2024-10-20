#!/usr/bin/env python3

from brain_games import even
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    name = even.welcome_user()
    even.parity_game(name)


if __name__ == '__main__':
    main()