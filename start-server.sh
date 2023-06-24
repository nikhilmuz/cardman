#!/usr/bin/env bash
python manage.py migrate
gunicorn -w 4 cardman.wsgi --bind 0.0.0.0:8000