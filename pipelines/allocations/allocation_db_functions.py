import psycopg2
import numpy as np
from psycopg2.extensions import connection as psy_connection, cursor as psy_cursor
from Code.Database_Connection.connections import testing_connection, account_name_correction



@testing_connection()
def create_allocations_table(*, conn: psy_connection, cursor: psy_cursor):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Account_Allocations (
            account_number VARCHAR(255) PRIMARY KEY, 
            semester VARCHAR(255),
            start_date DATE,
            end_date DATE,
            request FLOAT(2),
            rollover FLOAT(2),
            fundraising FLOAT(2),
            expenses FLOAT(2)
        );""")
    conn.commit()

def handle_row(row: list[str, float]):
    row = [float(i) if isinstance(i, np.float64) or isinstance(i, np.int64) else i for i in row]
    return row

@testing_connection()
def insert_rows(rows: list[list[str, float]], *, conn: psy_connection, cursor: psy_cursor):
    rows_string = ""
    for row in rows:
        row = handle_row(row)
        rows_string += f"{tuple(row)}, ".replace('"', "'")
    rows_string = rows_string.removesuffix(", ")
    cursor.execute(
        """INSERT INTO Account_Allocations (account_number, semester, start_date, end_date, request, rollover, fundraising, expenses)
        VALUES """+rows_string+
        """ON CONFLICT (account_number) DO NOTHING;"""
    )
    conn.commit()

