#!/usr/bin/env bash

# Number of worker threads
NUM_WORKERS=3

cd productivity &&
(gunicorn productivity.wsgi --user www-data --bind 0.0.0.0:8000 --workers $NUM_WORKERS &) &&
nginx -g "daemon off;"
