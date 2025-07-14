from pipelines.agency_reports.pipeline_agency_report import AgencyReportPipeline
from pipelines.organizations.pipeline_organization_info import OrganizationInfoPipeline

OrganizationInfoPipeline()
# AgencyReportPipeline()

# db_ag.reset_schema()

# read_org_info.ExcelOrganizationInfoReader().read_file(file_selector.file_selector())


# e = ebr.AgencyReportExtractor()
# file_path = r"E:\Projects\SGA_Financial_Reporting\data\raw_balance_reports\Agency Account Report 24-06-10.pdf"
# records = e.extract_files(file_selector.file_selector())

# for record in records:
#     report = tbr.format_pdf_content(record)
#     report = tbr.format_date_agency_report(report)
#     print(report['file_name'])
#     db_ag.add_agency_report(report)

