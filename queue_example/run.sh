#! /usr/bin.env sh

export PYTHONPATH=$PYTHONPATH:$(pwd)
export FLASK_APP=app/routes.py
export FLASK_ENV=develpoment

flask run


