import pandas as pd
import re
import os
import datetime
from typing import TypedDict

from utils.exceptions import FileNameException

from bases.base_reader import BaseReader
from bases.base_extractor import BaseExtractor
from bases.typed_dicts import AgencyReportDict

from pipelines.agency_reports.read_pdf_agency_reports import PdfAgencyReader
from pipelines.agency_reports.read_excel_agency_reports import ExcelAgencyReader
from pipelines.agency_reports.transform_agency_reports import format_pdf_content

def get_file_type(file_path: str) -> str:
    return file_path.split(".")[-1]

class AgencyReportExtractor(BaseExtractor):
    def __init__(self):
        super().__init__()
        self.date_match_str = r"\d\d.{1}\d\d.{1}\d{2,4}"

    @property
    def FILE_MAP(self):
        FILE_MAP: dict[str, BaseReader] = {
            "xlsx": ExcelAgencyReader(),
            "pdf": PdfAgencyReader()
        }
        return FILE_MAP

    def extract_files(self, file_paths: list[str]) -> list[AgencyReportDict]:
        """Reads multiple files.

        Args:
            file_paths (list[str]): List of file paths. 

        Returns:
            list[pd.DataFrame]: List of file contents to DataFrames. 
        """
        return [self.extract_file(file) for file in file_paths]

    def extract_file(self, file_path: str) -> AgencyReportDict:
        """Reads a file and outputs a pandas dataframe of the data. 

        Args:
            file_path (str): Path of file to read.

        Returns:
            pd.DataFrame: Pandas DataFrame based on file.
        """
        reader = self.get_reader(get_file_type(file_path))

        file_name = os.path.basename(file_path)

        agency_report: AgencyReportDict = {
            "file_name": file_name, 
            "date": self.read_date(file_name), 
            "dataframe": reader.read_file(file_path)
        }
        return agency_report

    def read_date(self, file_name: str) -> datetime.date:
        """Finds date in file name. All file names must contain a date in the form 'YY-MM-DD'.

        Args:
            file_name (str): File name of file (without path).

        Raises:
            FileNameException: Custom raise for when date cannot be found in the name. 

        Returns:
            datetime.date: Date time object of file report. 
        """
        date = re.search(self.date_match_str, file_name)
        if date is None:
            error_message = f"File Name \"{file_name}\" does not contain a valid date (YY-MM-DD). Each report must contain the date of the balance updates."
            raise FileNameException(error_message)
        
        return date[0]

