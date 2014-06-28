flask-celery-template
=====================

A besic template for creating a Flask frontend to Celery. The documentation for this integration
at http://flask.pocoo.org/docs/patterns/celery/ is a bit sparse so I put together this 
template that is used for both Flask and Celery. The nice thing about this template
is that it completely separates Flask and Celery into two separate modules and uses the 
standard module structure that is best for both Flask and Celery. It has served me pretty
well and I would reccomend it for others just getting into Flask and Celery.

In order to start Celery run: Celery -A celeryapp worker --loglevel=info
