import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Проверяет, является ли число четным."""
    return number % 2 == 0


def generate_round():
    """Генерирует раунд игры.

    Returns:
        tuple: (вопрос, правильный_ответ)
    """
    question = random.randint(1, 100)
    correct_answer = "yes" if is_even(question) else "no"
    return question, correct_answer
