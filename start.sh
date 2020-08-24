gunicorn -b 0.0.0.0:8080 DailyProphet:app
chromium-browser --start-fullscreen http://localhost:8080/gallery/