#!/bin/bash
gunicorn DailyProphet:app
chromium-browser --app=http://localhost:8080/gallery/ --start-fullscreen
