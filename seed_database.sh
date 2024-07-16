#!/bin/bash

rm db.sqlite3
rm -rf ./mdconverterapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations mdconverterapi
python3 manage.py migrate mdconverterapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

