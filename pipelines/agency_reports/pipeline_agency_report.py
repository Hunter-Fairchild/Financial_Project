from bases.base_pipeline import BasePipeline
from bases.typed_dicts import AgencyReportDict
from pipelines.agency_reports.extract_agency_reports import AgencyReportExtractor
from pipelines.agency_reports.transform_agency_reports import format_pdf_content, format_date_agency_report
from pipelines.agency_reports.load_agency_reports import add_agency_report

class AgencyReportPipeline(BasePipeline):
    def __init__(self, file_paths: list[str] = None):
        super().__init__(file_paths)
        records = self.extract()
        for i, record in enumerate(records):
            report = self.transform(record)
            self.print_progress(report["file_name"], i, len(records))
            self.load(report)

    def extract(self) -> list[AgencyReportDict]:
        return self.extractor.extract_files(self.file_paths)
    
    def transform(self, record: AgencyReportDict) -> AgencyReportDict:
        report = format_pdf_content(record)
        report = format_date_agency_report(report)
        return report
    
    def load(self, record: AgencyReportDict):
        add_agency_report(record)

    @property
    def extractor(self) -> AgencyReportExtractor:
        return AgencyReportExtractor()


if __name__ == "__main__":
    file_path = r"E:\Projects\SGA_Financial_Reporting\data\raw_balance_reports\Agency Account Report 24-06-10.pdf"
    AgencyReportPipeline()

