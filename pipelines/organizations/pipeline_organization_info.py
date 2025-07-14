import pandas as pd

from bases.base_pipeline import BasePipeline
from bases.typed_dicts import OrganizationInfoDict
from pipelines.organizations.extract_organization_information import OrganizationInfoExtractor
from pipelines.organizations.transform_organization_info import format_df_headers, add_creation_dates, fill_null_values

class OrganizationInfoPipeline(BasePipeline):
    def __init__(self, file_path: list[str] = None):
        super().__init__(file_path)
        records = self.extract()
        for i, record in enumerate(records):
            report = self.transform(record)
            self.print_progress(report["file_name"], i, len(records), report["dataframe"])
            # self.load(report)

    def extract(self):
        return self.extractor.extract_files(self.file_paths)

    def transform(self, record: OrganizationInfoDict) -> OrganizationInfoDict:
        record["dataframe"] = format_df_headers(record["dataframe"])
        record["dataframe"] = add_creation_dates(record["dataframe"])
        record["dataframe"] = fill_null_values(record["dataframe"])
        return record
    
    # def load(self, record: AgencyReportDict):
    #     add_agency_report(record)

    @property
    def extractor(self) -> OrganizationInfoExtractor:
        return OrganizationInfoExtractor()
