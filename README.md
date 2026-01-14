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

## Использование

После установки запустите игру командой:

```bash
brain-games
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
