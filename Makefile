.PHONY: all clean test

date=$(shell date +%F)

VIRTUAL_ENV=
unexport VIRTUAL_ENV

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9._-]+:.*?## / {printf "\033[1m\033[36m%-38s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

test: ## run pytest
	poetry run pytest -vvs

install: ## install dependencies and the package to poetry venv
	poetry install

lint: ## run mypy and flake8 to check the code
	poetry run mypy src
	poetry run flake8 src tests

fmt: ## run black to format the code
	poetry run black src tests
