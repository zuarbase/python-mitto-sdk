# include .env variables
include .env
export

all: build

env:
	echo $(PYPI_USERNAME)
	echo $(PYPI_TEST_PASSWORD)
	echo $(PYPI_PASSWORD)
.PHONY: env

build: clean
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
