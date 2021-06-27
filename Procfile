release: python manage.py migrate
web: gunicorn django_snippets.wsgi --log-file -
#worker: celery -A django_snippets worker -l info