import psycopg2
import numpy as np
import datetime
from psycopg2.extensions import connection as psy_connection, cursor as psy_cursor
from psycopg2.extras import execute_values

from pipelines.database_connections.connections import db_connection
from bases.typed_dicts import AgencyReportDict
from utils import helper_functions as helper_funcs

# Add in functionality for updating report amounts

@db_connection
def add_agency_report(agencyDict: AgencyReportDict, cursor: psy_cursor, conn: psy_connection):
    agency_id = create_agency_report(agencyDict, cursor, conn)
    
    if agency_id is None:
        return 

    acc_names_nos = agencyDict['dataframe'][["account_number", "account_name"]].copy()
    acc_names_nos["organization_id"] = None
    acc_names_nos["creation_date"] = helper_funcs.get_current_date()
    acc_names_nos["description"] = ""
    acc_names_nos = acc_names_nos[
        ["organization_id", "account_number", "account_name", "creation_date", "description"]
    ].rename({"account_name": "name"}, axis=1)

    account_list = list(acc_names_nos.itertuples(index=False, name=None))
    
    create_account(account_list, cursor, conn)

    balance_updates = agencyDict['dataframe'].rename({"account_name": "report_id", "balance_date": "date"}, axis=1)
    balance_updates["report_id"] = agency_id

    balance_updates = balance_updates.to_dict(orient="records")
    create_balance_updates(balance_updates, cursor, conn)

def create_balance_updates(balance_details: list[dict], cursor: psy_cursor, conn: psy_connection):
    with open("sql/create_balance_update.sql", "r") as file:
        cursor.executemany(file.read(), balance_details)

def create_account(account_details: list[tuple], cursor: psy_cursor, conn: psy_connection):
    with open("sql/create_account.sql", "r") as file:
        execute_values(cursor, file.read(), account_details)

def create_agency_report(agencyDict: AgencyReportDict, cursor: psy_cursor, conn: psy_connection):
    with open("sql/agency_report.sql", 'r') as file:
        cursor.execute(file.read(), {
            "file_name": agencyDict["file_name"],
            "date": agencyDict['date'],
            "uploaded_at": None
        })

    agency_id = cursor.fetchone()
    conn.commit()
    return agency_id[0] if agency_id is not None else None

@db_connection
def reset_schema(cursor, conn):
    with open("sql/schema.sql", 'r') as file:
        cursor.execute(file.read())
