# include .env variables
PACKAGE := src
include .env
export

all: build

env:
	echo $(PYPI_USERNAME)
	echo $(PYPI_TEST_PASSWORD)
	echo $(PYPI_PASSWORD)
.PHONY: env

build: pyenv flake8 pylint test coverage clean
	python3 setup.py sdist bdist_wheel
.PHONY: build

clean:
	rm -f dist/*
.PHONY: clean

develop: clean build
	pip install dist/*
.PHONY: develop

publish_test: clean build
	python3 -m twine upload --repository testpypi dist/* --username=$(PYPI_USERNAME) --password=$(PYPI_TEST_PASSWORD)
.PHONY: publish_test

publish: clean build
	python3 -m twine upload dist/* --username=$(PYPI_USERNAME) --password=$(PYPI_PASSWORD)
.PHONY: publish

version:
#ifndef part
#$(error part variable is not set - options: part=patch, part=minor, part=major)
#endif
	bumpversion $(part) setup.py
.PHONY: version_patch

flake8:
	flake8 $(PACKAGE) tests
.PHONY: flake8

pylint: pylint_pkg pylint_tests
.PHONY: pylint

pylint_pkg:
	pylint $(PACKAGE)
.PHONY: pylint_pkg

pylint_tests:
	pylint tests --disable=missing-docstring,duplicate-code,unused-argument
.PHONY: pylint_test

test:
	pytest -xv tests
.PHONY: test

coverage:
	pytest --cov=$(PACKAGE) --cov-report=term-missing --cov-fail-under=100 tests
.PHONY: coverage

freeze:
	pyenv/bin/pip freeze | egrep -v "$(PACKAGE)|flake8|pylint|pytest|pkg-resources" > requirements.txt
.PHONY: freeze

pyenv:
	virtualenv -p python3 pyenv
	pyenv/bin/pip install -r requirements.txt
.PHONY: pyenv
