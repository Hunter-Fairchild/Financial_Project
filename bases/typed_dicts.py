import datetime
import pandas as pd
from typing import TypedDict

class AccountDict(TypedDict):
    account_number: str
    account_name: str
    opening_balance: float
    cactivity: float
    ending_balance: float

class AgencyReportDict(TypedDict):
    file_name: str 
    date: str
    dataframe: pd.DataFrame

class OrganizationInfoDict(TypedDict):
    file_name: str 
    date: str
    dataframe: pd.DataFrame
