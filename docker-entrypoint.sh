#!/bin/sh
# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

echo "Make Migrations"

# all app migrations should go on a single line
# http://stackoverflow.com/questions/36153748/django-1-9-makemigrations-no-changes-detected
python manage.py makemigrations reddit users comments submissions


# Apply database migrations
echo "Apply database migrations"
python manage.py migrate reddit
python manage.py migrate users
python manage.py migrate comments
pythom manage.py migrate submissions


# Start server
echo "Starting server"
#python manage.py runserver '0.0.0.0:8000'
gunicorn django_reddit.wsgi:application --bind 0.0.0.0:8000
