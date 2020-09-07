.PHONY: app test migrate pro admin django

app:
	docker-compose run --rm app sh -c "python manage.py startapp ${app}"

test:
	docker-compose run --rm app sh -c "pytest -l -v -s ${app} && flake8"

migrate:
	docker-compose run --rm app sh -c "python manage.py makemigrations"
	docker-compose run --rm app sh -c "python manage.py migrate"

pro:
	docker-compose run --rm app sh -c "django-admin startproject ${pro} ."

admin:
	docker-compose run --rm app sh -c "python manage.py createsuperuser"

init:
	docker-compose run --rm app sh -c "python manage.py makemigrations shop"
	docker-compose run --rm app sh -c "python manage.py makemigrations cart"

restart:
	docker-compose restart
	docker-compose stop
	heroku container:login
	heroku container:push web -a new-ecsite
	heroku container:release web -a new-ecsite
	
