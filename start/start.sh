#! /bin/bash

mkdir /logs &&\
cd  /home/psycopg-test/ &&\
python3 -m pip install -r requirements.txt &&\
python3 main.py 600000
