import pandas as pd
import os
import Code.Database_Connection.records_db_functions as records_db
import Code.Database_Connection.category_db_functions as categories_db
import Code.Database_Connection.allocation_db_functions as allocations_db
from Code.file_selector import file_selector
from Code.record_file_reading import read_record_files
from Code.read_categories import get_categories
from Code.Allocations.allocation_file_reading import read_allocation_files


def load_from_files():
    files = [f"{file}" for file in file_selector()]
    records = pd.concat(read_record_files(files))

    upload_records(records)
    update_categories()

def update_allocations():
    allocations_path = "E:\\Projects\\SGA Project\\SGA_Allocations"

    files = [f"{allocations_path}\\{file}" for file in os.listdir(allocations_path)]
    allocations_df = pd.concat(read_allocation_files(files))

    allocations_db.create_allocations_table()
    allocations = [allocations_df.iloc[i, :].to_list() for i in range(allocations_df.shape[0])]
    allocations_db.insert_rows(allocations)


def update_categories():
    category_df = get_categories()
    categories_db.create_categories_table()
    
    categories = [category_df.iloc[i, :].to_list() for i in range(category_df.shape[0])]
    categories_db.insert_rows(categories)

def upload_records(records: pd.DataFrame):
    records_db.create_records_table()
    records = [records.iloc[i, :].to_list() for i in range(records.shape[0])]
    records_db.insert_rows(records)
