lint:
	flake8
celery:
	celery -A backend worker -B -l info
runserver:
	python manage.py runserver 0.0.0.0:8000
daphne:
	daphne -b 0.0.0.0 -p 8000 backend.asgi:channel_layer
worker:
	python manage.py runworker
migrate:
	python manage.py migrate
makemigrations:
	python manage.py makemigrations
