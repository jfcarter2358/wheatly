.PHONY: help lint test clean install install-dev docs

help:  ##        Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

install:  ##     Install poetry if needed and use it to install calligraphy
	pip install poetry
	poetry install --no-dev

install-dev:  ## Install poetry if needed and use it to install calligraphy and dev dependencies
	pip install poetry
	poetry install

lint:  ##        Format and lint calligraphy
	black wheatly
	pylint wheatly

release:  ##     Release the current version of calligraphy
	poetry build
	poetry publish -u "__token__" -p "$${PYPI_PASSWORD}"
