web: gunicorn config.wsgi:application
worker: celery worker --app=albert.taskapp --loglevel=info
