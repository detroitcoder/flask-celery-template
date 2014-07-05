from __future__ import absolute_import
from celery import Celery
from celeryapp import settings


def make_celery():
    """Instantiate and return the Celery() instance and perform the modification to the
    TaskBase class so that it is configured for Flask.

    details here: http://flask.pocoo.org/docs/patterns/celery/
    """

    celery_instance = Celery("celeryapp",
                             broker='amqp://guest@localhost//',
                             backend='amqp://',
                             include=['celeryapp.tasks'])
    celery_instance.config_from_object(settings.config)

    # # modify the TaskBase class
    # TaskBase = celery_instance.Task
    # class ContextTask(TaskBase):
    #     abstract = True
    #     def __call__(self, *args, **kwargs):
    #         with app.app_context():
    #             return TaskBase.__call__(self, *args, **kwargs)
    # celery_instance.Task = ContextTask
    return celery_instance

celery_app = make_celery()

if __name__ == '__main__':
    celery_app.start()