#! /bin/bash

git clone https://github.com/nanaones/psycopg-test &&\
git clone https://github.com/vishnubob/wait-for-it /wait &&\

## get env if run as docker-compose
## TODO add if connectPgcontainer, connect elasticContainer and  fluentdContainer 

# wait-for-it

# mkdir /logs &&\
chmod +x ./wait/wait-for-it.sh &&\
./wait/wait-for-it.sh 127.0.0.1:5432 &&\
echo $CONFIGPATH &&\
cd  /psycopg-test/ &&\
cp /run/config/config.ini /psycopg-test/config/config.ini &&\
python3 -m pip install -r requirements.txt &&\
python3 main.py  $loop