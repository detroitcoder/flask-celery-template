from __future__ import absolute_import
from  celeryapp.celery import celery_app


@celery_app.task
def add_numbers(x, y):
    """This becomes a task that is managed by celery and is referenced in
    views.py."""

    return "{} plus {} equals {}".format(x, y, x+y)