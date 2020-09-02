.PHONY: app test migrate pro admin django

app:
	docker-compose run --rm app sh -c "python manage.py startapp ${name}"

test:
	docker-compose run --rm app sh -c "pytest -l -v -s ${app}"

migrate:
	docker-compose run --rm app sh -c "python manage.py makemigrations"
	docker-compose run --rm app sh -c "python manage.py migrate"

pro:
	docker-compose run --rm app sh -c "django-admin startproject ${pro} ."

admin:
	docker-compose run --rm app sh -c "python manage.py createsuperuser"
