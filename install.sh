#!/usr/bin/env sh

npm install
npm run build
pip install python-dotenv

sudo apt install gunicorn