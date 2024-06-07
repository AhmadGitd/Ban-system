#!/bin/sh

cd html/

export FLASK_APP=/html/app.py
export FLASK_DEBUG=1
export FLASK_ENV=development


python3 -m flask run --host=0.0.0.0 --port=8002
