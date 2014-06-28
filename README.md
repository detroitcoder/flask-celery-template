flask-celery-template
=====================

A besic template for creating a Flask frontend to Celery.

The <a href="http://flask.pocoo.org/docs/patterns/celery/">documentation</a> for Celery and Flask integration 
while sufficient is a bit sparse. So I put together this 
template that can be used for both Flask and Celery. The nice thing about this template
is that it completely separates Flask and Celery into two separate modules and uses the 
standard module structure that is best for both Flask and Celery. It has served me pretty
well and I would reccomend it for others just getting into Flask and Celery.

To start:

1. Celery run: Celery -A celeryapp worker --loglevel=info
2. python startflask.py
3. python tests.py

