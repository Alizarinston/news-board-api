release: echo $CONFIG | base64 -d > ./config/config.ini && python manage.py migrate
web: echo $CONFIG | base64 -d > ./config/config.ini && (celery -A config worker -l INFO & celery -A config beat -l INFO & gunicorn config.wsgi -b 0.0.0.0:$PORT --workers=3)
