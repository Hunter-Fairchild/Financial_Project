import psycopg2
from psycopg2.extensions import connection as psy_connection, cursor as psy_cursor
import functools
import os
from dotenv import load_dotenv

load_dotenv()

credentials = {
    "database": os.getenv("DATABASE"), 
    "user": os.getenv("USER"), 
    "host": os.getenv("HOST"), 
    "password": os.getenv("PASSWORD"), 
    "port": os.getenv("PORT")
}


def db_connection(func):
    def wrapper(*args, **kwargs):
        with psycopg2.connect(**credentials) as conn:
            with conn.cursor() as cursor:
                return func(*args, conn=conn, cursor=cursor, **kwargs)
    return wrapper
