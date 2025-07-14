import pandas as pd
from pipelines.organizations.extract_organization_information import OrganizationInfoExtractor
from utils.helper_functions import get_current_date


def format_df_headers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename({
        col: col.replace(" ", "_").lower() for col in df.columns}, axis=1)
    return df

def add_creation_dates(df: pd.DataFrame) -> pd.DataFrame:
    df["creation_date"] = get_current_date()
    return df

def fill_null_values(df: pd.DataFrame) -> pd.DataFrame:
    df["funding_category"] = df["funding_category"].fillna("No Funding Category")
    df["advisor"] = df["advisor"].fillna("No Advisor")
    df["member_count"] = df["member_count"].fillna(0)
    df["description"] = df["description"].fillna("")
    return df
