release: python manage.py migrate
release: python manage.py collectstatic --noinput'
web: gunicorn django_snippets.wsgi
#worker: celery -A django_snippets worker -l info