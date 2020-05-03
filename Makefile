# Makefile

install:
	poetry install
lint:
	poetry run flake8
test:
	
publish:
	poetry build
	poetry publish -r testpypi

run:
	poetry run python manage.py runserver
