from RequestsToDB import RequestsToDB
from DB import pg_query, pg_query_pool
import Decorator

import time

class MainClass:

    def __init__(self, _loop=100):
        self._loop = _loop
        self.query = RequestsToDB().config_data.get("SQL", 
                                                    "INSERT")
        
    @Decorator.time_print
    def loop_query_pool(self, _message="pool"):
        for _num in range(self._loop):
            pg_query_pool(_query=str(self.query).replace("?", 
                                                         f"'{_message} - {str(_num)}'"),
                                                         _save = True, _log_save_folder_path="./log/")        

    @Decorator.time_print
    def loop_query(self, _message="basic"):
        for _num in range(self._loop):
            pg_query(_query=str(self.query).replace("?", 
                                                    f"'{_message} - {str(_num)}'"),
                                                         _save = True)        


if __name__ == "__main__":
    main = MainClass(_loop=1000)
    main.loop_query_pool()
    main.loop_query()
    