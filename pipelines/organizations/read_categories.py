import pandas as pd

def get_categories() -> pd.DataFrame:
    categories = pd.read_excel("Storage/organization_categories.xlsx")
    categories = categories.fillna("No Known Category")
    return categories

