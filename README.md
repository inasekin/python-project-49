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
