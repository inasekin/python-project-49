import operator
import random

DESCRIPTION = "What is the result of the expression?"

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}
MIN_NUMBER = 1
MAX_NUMBER = 100


def calculate(num1, num2, operation):
    """Вычисляет результат математической операции.

    Args:
        num1: первое число
        num2: второе число
        operation: операция (+, -, *)

    Returns:
        int: результат вычисления
    """
    return OPERATIONS[operation](num1, num2)


def generate_round():
    """Генерирует раунд игры.

    Returns:
        tuple: (вопрос, правильный_ответ)
    """
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(list(OPERATIONS.keys()))

    question = f"{num1} {operation} {num2}"
    correct_answer = str(calculate(num1, num2, operation))

    return question, correct_answer
