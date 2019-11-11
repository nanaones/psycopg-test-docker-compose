FROM nanaones/psycopg-test:0.0.2
    
 ADD . /home/psycopg-test/
 CMD ["bash", "/home/psycopg-test/start/start.sh"]