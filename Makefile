.PHONY: all clean test

date=$(shell date +%F)

all:

VIRTUAL_ENV=
unexport VIRTUAL_ENV

test:
	poetry run pytest -vvs
install :
	poetry install
