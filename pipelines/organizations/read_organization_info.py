import pandas as pd

from bases.base_reader import BaseReader

class ExcelOrganizationInfoReader(BaseReader):
    def __init__(self):
        super().__init__()

    def read_file(self, file_path: str):
        df = pd.read_csv(file_path)
        return df


