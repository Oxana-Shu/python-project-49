#!/usr/bin/env python3

from brain_games.games import prime
from brain_games.games import logical


def main():
    print('Welcome to the Brain Games!')
    name = logical.welcome_user()
    prime.prime_game(name)


if __name__ == '__main__':
    main()
