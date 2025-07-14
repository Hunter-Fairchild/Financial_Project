import os

from bases.base_extractor import BaseExtractor, BaseReader
from bases.typed_dicts import OrganizationInfoDict

from utils.helper_functions import get_file_type

from pipelines.organizations.read_organization_info import ExcelOrganizationInfoReader

class OrganizationInfoExtractor(BaseExtractor):
    def __init__(self):
        super().__init__()

    def extract_file(self, file_path):
        reader = self.get_reader(get_file_type(file_path))

        file_name = os.path.basename(file_path)

        organization_info: OrganizationInfoDict = {
            "file_name": file_name, 
            "date": self.read_date(file_name), 
            "dataframe": reader.read_file(file_path)
        }
        return organization_info
    
    def extract_files(self, file_paths):
        return [self.extract_file(file) for file in file_paths]

    @property
    def FILE_MAP(self):
        FILE_MAP: dict[str, BaseReader] = {
            "xlsx": ExcelOrganizationInfoReader(),
        }
        return FILE_MAP
