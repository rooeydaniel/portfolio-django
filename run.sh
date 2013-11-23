#!/bin/bash

django-admin.py collectstatic --noinput --pythonpath=$PWD
django-admin.py runserver 0.0.0.0:8001 --pythonpath=$PWD
