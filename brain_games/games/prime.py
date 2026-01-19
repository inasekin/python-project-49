import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    """Проверяет, является ли число простым.

    Args:
        number: число для проверки

    Returns:
        bool: True если число простое, False иначе
    """
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


def generate_round():
    """Генерирует раунд игры.

    Returns:
        tuple: (вопрос, правильный_ответ)
    """
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_prime(question) else "no"

    return question, correct_answer
