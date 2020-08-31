#!/bin/sh
virtualenv venv --python=python3.7
source venv/bin/activate
pip install flask 
pip install Flask-RESTful
pip install Flask-JWT
python code/app.py
