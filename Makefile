lint:
	black --check .
	flake8 --max-complexity 10
	mypy --sqlite-cache .
	isort --check-only .

test:
	pytest

check: lint test

format_code:
	isort .
	black .