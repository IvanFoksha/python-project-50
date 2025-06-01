install:
	uv sync

check: lint test

lint:
	uv run ruff .

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_code --cov-report=xml
