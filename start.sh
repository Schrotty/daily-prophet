#!/usr/bin/env sh

gunicorn -w 2 -b 127.0.0.1:8080 DailyProphet:app