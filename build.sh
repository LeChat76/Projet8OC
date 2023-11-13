#!/bin/bash


cd /P8

# Install dependancies
/opt/render/project/src/.venv/bin/python3.7 -m pip install --upgrade pip
/opt/render/project/src/.venv/bin/python3.7 -m pip install -r requirements.txt

# Collect static files
/opt/render/project/src/.venv/bin/python3.7 manage.py collectstatic --noinput

# launch web service
gunicorn lechat76_site.wsgi

