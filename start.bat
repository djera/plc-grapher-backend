python manage.py makemigrations --settings=backend.settings
python manage.py migrate --settings=backend.settings
python manage.py runserver 0.0.0.0:8000 --settings=backend.settings
