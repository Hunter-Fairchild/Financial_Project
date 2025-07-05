import pipelines.agency_reports.extract_agency_reports as ebr
import utils.file_selector as file_selector
import pipelines.agency_reports.transform_agency_reports as tbr
import pipelines.agency_reports.agency_reports_db_functions as db_ag
import pipelines.organizations.read_organization_info as read_org_info

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

