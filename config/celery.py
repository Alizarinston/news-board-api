import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery(__file__)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "reset-upvotes": {
        "task": "reset_upvotes",
        "schedule": crontab(minute="0", hour="0"),
    }
}
