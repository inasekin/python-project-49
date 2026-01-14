install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check --fix brain_games

format:
	uv run ruff format brain_games

.PHONY: install brain-games build package-install package-reinstall lint lint-fix format
