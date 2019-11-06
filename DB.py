import psycopg2
from psycopg2 import pool
from RequestsToDB import RequestsToDB

def pg_query( _query, 
            user = RequestsToDB().config_data.get("DB", "user"), 
            password = RequestsToDB().config_data.get("DB", "password"),
            host = RequestsToDB().config_data.get("DB", "host"),
            port = RequestsToDB().config_data.get("DB", "port"),
            database = RequestsToDB().config_data.get("DB", "database"),
            _printing = False,
            _return = False
             ):
    if _printing:
        print(user)
        print(password)
        print(host)
        print(port)
        print(database)
    try:
        connection = psycopg2.connect(user=user.replace('"',""),
                                        password=password.replace('"',""),
                                        host=host.replace('"',""),
                                        port=int(port.replace('"',"")),
                                        database=database.replace('"',""))
        cursor = connection.cursor()
        cursor.execute(_query)
        connection.commit()
        if _printing:
            print("successfully connect to PostgreSQL ")

        if _return:
            rows = cursor.fetchall()
            if len(rows)>0:
                return rows
            
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting PostgreSQL", error)
        
    finally:
        if (connection):
            cursor.close()
            connection.close()
            if _printing:
                print("PostgreSQL connection is closed")
            
def pg_query_pool( 
            _query, 
            user = RequestsToDB().config_data.get("DB", "user"), 
            password = RequestsToDB().config_data.get("DB", "password"),
            host = RequestsToDB().config_data.get("DB", "host"),
            port = RequestsToDB().config_data.get("DB", "port"),
            database = RequestsToDB().config_data.get("DB", "database"),
            _printing = False,
            _return = False
             ):

    try:
        postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(
                                                             1, 
                                                             20,
                                                             user=user,
                                                             password=password,
                                                             host=host,
                                                             port=port,
                                                             database=database
                                                             )
        print(postgreSQL_pool)
        if(postgreSQL_pool):
            print("Connection pool created successfully")

        # Use getconn() to Get Connection from connection pool
        ps_connection  = postgreSQL_pool.getconn()

        if(ps_connection):
            print("successfully recived connection from connection pool ")
            ps_cursor = ps_connection.cursor()
            ps_cursor.execute(_query)
            mobile_records = ps_cursor.fetchall()

            print ("Displaying rows from mobile table")
            for row in mobile_records:
                print (row)

            ps_cursor.close()

            #Use this method to release the connection object and send back to connection pool
            postgreSQL_pool.putconn(ps_connection)
            print("Put away a PostgreSQL connection")

    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while connecting to PostgreSQL", error)

    finally:
        #closing database connection.
        # use closeall method to close all the active connection if you want to turn of the application
        if (postgreSQL_pool):
            postgreSQL_pool.closeall
        print("PostgreSQL connection pool is closed")
    