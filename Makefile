# Makefile

install:
	python3 -m poetry install
lint:
	python3 -m poetry run flake8
test:
	python3 -m poetry run coverage run --source='.' --omit '.venv/*' manage.py test
	python3 -m poetry run coverage report
	python3 -m poetry run coverage xml
	
publish:
	python3 -m poetry build
	python3 -m poetry publish -r testpypi

run:
	python3 -m poetry run python manage.py runserver

requirements:
	python3 -m poetry export -f requirements.txt -o requirements.txt

