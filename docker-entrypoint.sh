#!/bin/sh
# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

echo "Make Migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
#python manage.py runserver '0.0.0.0:8000'
gunicorn django_reddit.wsgi:application --bind 0.0.0.0:8000
