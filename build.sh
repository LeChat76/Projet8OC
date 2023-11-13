#!/bin/bash


# Install dependancies
/opt/render/project/src/.venv/bin/python3.7 -m pip install --upgrade pip

# Collect static files
/opt/render/project/src/.venv/bin/python3.7 manage.py collectstatic --noinput
