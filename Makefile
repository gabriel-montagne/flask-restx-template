.venv:  # creates .venv folder if does not exist
	python3 -m venv .venv


.venv/bin/pip: .venv # installs latest pip
	.venv/bin/pip install -U pip setuptools


install: .venv/bin/pip
	.venv/bin/pip install -r requirements.txt


start_db:
	docker-compose up -d


run:
	export FLASK_APP=main.py \
	&& flask run


run_docker:
	docker-compose up


pep8:
	. .venv/bin/activate && flake8 --ignore E501


test: start_db
	export APP_ENV=test && \
	.venv/bin/pytest -p no:warnings --cov app --cov-report html --cov-report term
	open -a 'Google Chrome' './htmlcov/index.html'