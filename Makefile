install:
	poetry install

.PHONY: gendiff
gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip3 install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

pinstall: build package-install
