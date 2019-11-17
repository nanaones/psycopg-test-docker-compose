FROM nanaones/psycopg-test:0.0.4

ENV loop 1

ADD ./start /run
CMD ["bash", "/run/start.sh"]