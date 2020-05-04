# Makefile

install:
	poetry install
lint:
	poetry run flake8
test:
	poetry run coverage run --omit '.venv/*' manage.py test
	poetry run coverage report
	poetry run coverage xml
	
publish:
	poetry build
	poetry publish -r testpypi

run:
	poetry run python manage.py runserver

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate
