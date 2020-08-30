migrate:
	python manage.py makemigrations
	python manage.py migrate

app:
	python manage.py startapp ${name}

test:
	pytest -l -v -s ${app}
