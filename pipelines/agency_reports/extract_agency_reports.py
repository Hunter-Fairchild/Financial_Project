import os

from utils.helper_functions import get_file_type

from bases.base_reader import BaseReader
from bases.base_extractor import BaseExtractor
from bases.typed_dicts import AgencyReportDict

from pipelines.agency_reports.read_pdf_agency_reports import PdfAgencyReader
from pipelines.agency_reports.read_excel_agency_reports import ExcelAgencyReader

class AgencyReportExtractor(BaseExtractor):
    def __init__(self):
        super().__init__()

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



