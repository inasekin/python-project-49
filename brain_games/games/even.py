import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number):
    """Проверяет, является ли число четным."""
    return number % 2 == 0


def generate_round():
    """Генерирует раунд игры.

    Returns:
        tuple: (вопрос, правильный_ответ)
    """
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_even(question) else "no"
    return question, correct_answer
