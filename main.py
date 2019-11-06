from RequestsToDB import RequestsToDB
from DB import pg_query, pg_query_pool
import time
import asyncio


    
class main:


    def __init__(self, _loop=100):
        
        self._loop = _loop
        self.query = RequestsToDB.config_data.get("QUERY", "Query")
        
    def loop_query_pool(_message="pool"):
        # _query = 
        for _num in self._loop:
            pg_query_pool(_query=str(self.query).replace("?", _message + str(_num)))
            
    def loop_query(_message="basic"):
        for _num in self._loop:
            pg_query(_query=str(self.query).replace("?", _message + str(_num)))

if __name__ == "__main__":
    mainClass = main(_loop=10000)
    mainClass.loop_query_pool()
    mainClass.loop_query()
    