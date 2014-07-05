flask-celery-template
=====================

A besic template for creating a Flask frontend to Celery.

In this template the application context is not used for Flask

To start:

    Celery -A celeryapp worker --loglevel=info
    python startflask.py
    python tests.py

