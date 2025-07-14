import psycopg2
import numpy as np
import datetime
from psycopg2.extensions import connection as psy_connection, cursor as psy_cursor
from psycopg2.extras import execute_values

from pipelines.database_connections.connections import db_connection
from bases.typed_dicts import OrganizationInfoDict
from utils import helper_functions as helper_funcs

@testing_connection()
def create_categories_table(*, conn: psy_connection, cursor: psy_cursor):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Account_Categories (
            account_number VARCHAR(255) PRIMARY KEY, 
            account_name VARCHAR(255),
            account_category VARCHAR(255)
        );""")
    conn.commit()

@testing_connection()
def insert_rows(rows: list[list[str, float]], *, conn: psy_connection, cursor: psy_cursor):
    rows_string = ""
    for row in rows:
        row[1] = account_name_correction(row[1])
        rows_string += f"{tuple(row)}, ".replace('"', "'")
    rows_string = rows_string.removesuffix(", ")
    cursor.execute(
        """INSERT INTO Account_Categories (account_number, account_name, account_category)
        VALUES """+rows_string+
        """ON CONFLICT (account_number) DO NOTHING;"""
    )
    conn.commit()

