lint:
	black --check .
	flake8
	mypy --sqlite-cache .
	isort --check-only .

test:
	coverage run -m pytest
	coverage report

check: lint test

format_code:
	isort .
	black .