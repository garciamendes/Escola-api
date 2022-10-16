PROJECT := setup

clean:
	./manage.py clean_pyc

requirements-dev:
	pip install -r requirements/develop.txt

runserver:
	./manage.py runserver 0.0.0.0:8000

migrate:
	./manage.py migrate

migrations:
	./manage.py makemigrations

showmigrations:
	./manage.py showmigrations

urls:
	./manage.py show_urls

urls-api:
	./manage.py show_urls | grep -i api

shell:
	./manage.py shell_plus

shell-sql:
	./manage.py shell_plus --print-sql

collectstatic:
	./manage.py collectstatic

superuser:
	./manage.py createsuperuser
