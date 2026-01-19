#!/usr/bin/env python3
"""Скрипт для запуска игры арифметическая прогрессия."""

from brain_games.engine import run_game
from brain_games.games import progression


def main():
    """Запускает игру арифметическая прогрессия."""
    run_game(progression)


if __name__ == "__main__":
    main()
