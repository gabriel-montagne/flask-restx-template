.venv:  # creates .venv folder if does not exist
	python3 -m venv .venv


.venv/bin/pip: .venv # installs latest pip
	.venv/bin/pip install -U pip setuptools


alembic/init:
	alembic init models/database/alembic


alembic/revision:  		# make alembic/revision comment=new_revision
	alembic revision --autogenerate -m ${comment}


alembic/migrations:		# make alembic/migrations env=dev
	@(export PYTHONPATH=$(shell pwd) && export APP_ENV=${env} && alembic upgrade head)


install: .venv
	.venv/bin/pip install -r requirements.txt


start_db:
	docker-compose up -d


init:
	python manage.py db init


migrate:		# make migrate m=comment
	python manage.py db migrate -m ${m}


upgrade:
	python manage.py db upgrade


run:
	python manage.py run


pep8:
	. .venv/bin/activate && flake8 --ignore E501 ghibli_project


test: start_db
	export APP_ENV=test && \
	.venv/bin/pytest -p no:warnings --cov app --cov-report html --cov-report term
	open -a 'Google Chrome' './htmlcov/index.html'