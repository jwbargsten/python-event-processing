.PHONY: all clean test

date=$(shell date +%F)

VIRTUAL_ENV=
unexport VIRTUAL_ENV

test:
	poetry run pytest -vvs
install :
	poetry install
lint:
	poetry run mypy src
	poetry run flake8 src tests
fmt:
	poetry run black src tests
