#! /bin/bash

echo $CONFIGPATH &&\
echo $DBMS_ADDRESS &&\
echo $DBMS_PORT &&\
echo $CONFIGPATH &&\
/run/chekLogFolder.sh &&\
git clone https://github.com/nanaones/psycopg-test &&\
cd  /psycopg-test/ &&\
python3 -m pip install -r requirements.txt &&\
python3 main.py  $loop $minconn $_log_save_folder_path $_log_type