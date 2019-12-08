# psycopg-test-docker-compose

 [psycopg-test](https://github.com/nanaones/psycopg-test) 가 작업을 수행한 후 남는 로그 파일에 대한 실시간 분석을 위한 Docker-Compose 입니다. 

---

## Index
 1. [Requirenment](https://github.com/nanaones/psycopg-test-docker-compose#Requirenment)
 2. [Containers](https://github.com/nanaones/psycopg-test-docker-compose#Containers)
 2. [Start](https://github.com/nanaones/psycopg-test-docker-compose#Start)
 3. [Config](https://github.com/nanaones/psycopg-test-docker-compose#Config)
 4. [How_to_check](https://github.com/nanaones/psycopg-test-docker-compose#How_to_check)  
 5. [Customize](https://github.com/nanaones/psycopg-test-docker-compose#Customize)


---

## 1. Requirenment  

* [`DockerDesktop`](https://www.docker.com/products/docker-desktop)  

## 2. Containers
1. Python-main  
    - PostgresSQL 컨테이너를 향한 SQL 쿼리 실행
    - 통신소요시간을 Log파일로서 기록한다.[config 옵션에 따라 `json`, `csv` 확장자 선택가능(기본:`json`)]
        - log파일 저장 위치:
            - `./docker-compose/log/`
2. PostgresSQL   
    - `./docker-compose/query/query.sql`이 초기 쿼리로서 수행된다.
3. Fluentd  
    - `./docker-compose/log/`내의 파일들을 tail 한다.
    - tail된 결과물은 ElasticSearch 컨테이너로 보내진다.
    - pos_file path :  
        - `./docker-compose/log/fluentd-log.pos`
4. ElasticSearch 
    - 검색엔진으로 사용된다.
    - Fluentd 로부터 전달받은 내용을 구분한다.
5. Prometheus  
    - exporter 들을 통해 각 container들의 상태를 기록한다.
6. Grafana
    - ElasticSearch에 연결하여 데이터를 시각화한다.
    - Prometheus에 접속하여 전체 컨테이너들의 상태 데이터를 시각화한다.  
6. Prometheus - exporters  
    - Fluentd-exporter 
        - Fluentd 컨테이너가 읽는 상태를 Prometheus에게 보낸다.
        - Fluentd 컨테이너가 보내는 상태를 Prometheus에게 보낸다. 
        - 컨테이너의 상태를 Prometheus에게 보낸다.
    - PostgresSQL-exporter 
        - DB의 상태정보를 Prometheus에게 보낸다.
        - 컨테이너의 상태 정보를 Prometheus에게 보낸다.


## 2. Start 

`Run composefile`  
```
 $ docker-compose up --build
```

## 3. Config

1. Python-main container config  
    - `./psycopg-config/config/config.ini`

```ini
$ cat  ./psycopg-config/config/config.ini

[SQL]
INSERT = INSERT INTO public.t_test(c_test) VALUES (?);

[DB]
user=postgres
password=1234
host=db-postgres
port=5432
database=postgres

[TIME]
timeZone=Asia/Seoul

[LOG]
logSave=True
logSavePath=/logs/
logType=json
```

`About TimeZone`,   
You can run this code to output a list of available TimeZones.    
```python
import pytz

pytz.all_timezones
```

By default,   
*  The default save path for logs is determined by the log.logSavePath value in `./config/config.ini`.  
*  logs are stored( in `./logs` path ) as follows:  


1. json

```json

{"now" : "%Y-%m-%d %H:%M:%s+%Z", "start" : "%Y-%m-%d %H:%M:%s", "end" : "%Y-%m-%d %H:%M:%s", "time" : "%s"} \n
```

2. csv

``` csv
"%Y-%m-%d %H:%M:%s+%Z", "%Y-%m-%d %H:%M:%s", "%Y-%m-%d %H:%M:%s", "%s" \n
```

---
2. fluentd-config file
    - `./fluentd/fluent.conf`
    - Fluentd container tail logfiles. 

---
3. prometheus.yml
    - `./prometheus.yml`
--- 

## 4. How_to_check
TBD  

## 5. Customize
TBD
