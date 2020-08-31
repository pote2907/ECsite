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

django:
	docker-compose run --rm app sh -c "django-admin startproject app ."
	
init:
	docker-compose run --rm app sh -c "python manage.py makemigrations shop"
	docker-compose run --rm app sh -c "python manage.py makemigrations cart"
	
