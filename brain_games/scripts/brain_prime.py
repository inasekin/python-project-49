#!/usr/bin/env python3
"""Скрипт для запуска игры простое ли число."""

from brain_games.engine import run_game
from brain_games.games import prime


def main():
    """Запускает игру простое ли число."""
    run_game(prime)


if __name__ == "__main__":
    main()
