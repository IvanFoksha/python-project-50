install:
	uv sync

check: lint test

lint:
	uv run python -m ruff check .

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_code --cov-report=xml
