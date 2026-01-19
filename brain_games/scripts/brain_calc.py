#!/usr/bin/env python3
"""Скрипт для запуска игры калькулятор."""

from brain_games.engine import run_game
from brain_games.games import calc


def main():
    """Запускает игру калькулятор."""
    run_game(calc)


if __name__ == "__main__":
    main()
