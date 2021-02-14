from celery import shared_task
from .models import Post


@shared_task(name="reset_upvotes")
def reset_upvotes():
    Post.objects.all().update(upvotes=0)
