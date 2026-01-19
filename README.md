# Brain Games

### Hexlet tests and linter status:

[![Actions Status](https://github.com/inasekin/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/inasekin/python-project-49/actions)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=inasekin_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=inasekin_python-project-49)

## Описание

Brain Games - набор мини-игр для тренировки ума, запускаемых из консоли.

## Установка

```bash
# Клонирование репозитория
git clone https://github.com/inasekin/python-project-49.git
cd python-project-49

# Установка зависимостей
make install

# Сборка пакета
make build

# Установка пакета
make package-install
```

## Игры

### brain-even - Проверка на чётность

Пользователю показывается случайное число. Нужно ответить `yes`, если число чётное, или `no` — если нечётное.

```bash
brain-even
```

### brain-calc - Калькулятор

Пользователю показывается случайное математическое выражение (например, `35 + 16`), которое нужно вычислить и записать правильный ответ.

```bash
brain-calc
```

### brain-gcd - Наибольший общий делитель (НОД)

Пользователю показывается два случайных числа. Нужно вычислить и ввести наибольший общий делитель этих чисел.

```bash
brain-gcd
```

### brain-progression - Арифметическая прогрессия

Показывается ряд чисел, образующий арифметическую прогрессию, одно из чисел заменено на `..`. Нужно определить это число.

```bash
brain-progression
```

### brain-prime - Простое ли число?

Пользователю показывается случайное число. Нужно ответить `yes`, если число простое, или `no` — если составное.

```bash
brain-prime
```

## Примеры игр

### Игра "Проверка на чётность"

Запустите игру:

```bash
brain-even
```

Пример успешной игры:

```
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: no
Correct!
Question: 6
Your answer: yes
Correct!
Question: 7
Your answer: no
Correct!
Congratulations, Sam!
```

### Игра "Калькулятор"

Запустите игру:

```bash
brain-calc
```

Пример успешной игры:

```
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What is the result of the expression?
Question: 4 + 10
Your answer: 14
Correct!
Question: 25 - 11
Your answer: 14
Correct!
Question: 25 * 7
Your answer: 175
Correct!
Congratulations, Sam!
```

### Игра "НОД"

Запустите игру:

```bash
brain-gcd
```

Пример успешной игры:

```
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Find the greatest common divisor of given numbers.
Question: 25 50
Your answer: 25
Correct!
Question: 100 52
Your answer: 4
Correct!
Question: 3 9
Your answer: 3
Correct!
Congratulations, Sam!
```

### Игра "Арифметическая прогрессия"

Запустите игру:

```bash
brain-progression
```

Пример успешной игры:

```
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What number is missing in the progression?
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 15
Correct!
Question: 2 5 8 .. 14 17 20 23 26 29
Your answer: 11
Correct!
Question: 14 19 24 29 34 39 44 49 54 ..
Your answer: 59
Correct!
Congratulations, Sam!
```

### Игра "Простое ли число?"

Запустите игру:

```bash
brain-prime
```

Пример успешной игры:

```
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 7
Your answer: yes
Correct!
Question: 4
Your answer: no
Correct!
Question: 23
Your answer: yes
Correct!
Congratulations, Sam!
```

## Разработка

```bash
# Запуск без установки
make brain-games

# Проверка кода линтером
make lint

# Автоматическое исправление ошибок
make lint-fix

# Форматирование кода
make format

# Пересборка и переустановка
make build
make package-reinstall
```
