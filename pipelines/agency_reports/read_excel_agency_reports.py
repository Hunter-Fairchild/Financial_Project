import pandas as pd

from bases.base_reader import BaseReader


class ExcelAgencyReader(BaseReader):
    def __init__(self):
        self.headers = ['account_number', 'account_name', 'opening_balance', 'cactivity', 'ending_balance']

    def read_file(self, file_path: str) -> pd.DataFrame:
        df = pd.read_excel(file_path)
        df.columns = self.headers
        return df


if __name__ == "__main__":
    path = r"E:\Projects\SGA_Financial_Reporting\data\raw_balance_reports\Agency Account Report 24-06-03.xlsx"
    e = ExcelAgencyReader()
    print(e.read_file(path))

