import datetime
import pandas as pd

from bases.typed_dicts import AgencyReportDict


balance_map_table = str.maketrans({
    ",": '',
    "(": "-", 
    ")": ""
})


def format_pdf_content(agency_report: AgencyReportDict) -> AgencyReportDict:
    """Formats content from the pdf version of the agency accounts report, after it has been read. 
    Removes extra waste from name, and replaces invalid chars from balance strings and makes them floats. 

    Args:
        df (pd.DataFrame): DataFrame from the pdf file

    Returns:
        pd.DataFrame: Formatted dataframe from pdf file 
    """
    df = agency_report['dataframe']
    df["account_name"] = df["account_name"].str.rsplit(" - ", n=1).str[0]

    balance_cols = ["opening_balance", "cactivity", "ending_balance"]
    df[balance_cols] = df[balance_cols].map(lambda s: float(str(s).translate(balance_map_table)))

    return agency_report

def format_date_agency_report(agency_report: AgencyReportDict) -> AgencyReportDict:
    """Updates all dates in an AgencyReportDict. 
    Formats date in dict and adds a pd.Timestamp to the dataframe. 

    Args:
        agency_report (AgencyReportDict): AgencyReportDict

    Returns:
        AgencyReportDict: AgencyReportDict with formatted dates
    """
    if len(agency_report['date'].split("-", maxsplit=1)) != 4:
        agency_report['date'] = "20" + agency_report['date']
    
    agency_report['dataframe'].insert(2, "balance_date", pd.Timestamp(agency_report['date']).date())
    return agency_report
