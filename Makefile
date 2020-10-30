# include .env variables
ifneq (,$(wildcard ./.env))
	include .env
	export
endif

all: build

build: clean
	python3 setup.py sdist bdist_wheel
.PHONY: build

clean:
	rm -f dist/*
.PHONY: clean

develop: clean build
	pip install dist/*
.PHONY: develop

publish: clean build
	python3 -m twine upload --repository testpypi dist/* --username=$(TWINE_USERNAME) --password=$(TWINE_PASSWORD)
.PHONY: publish

version:
#ifndef part
#$(error part variable is not set - options: part=patch, part=minor, part=major)
#endif
	bumpversion $(part) setup.py
.PHONY: version_patch
