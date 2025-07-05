from bases.base_extractor import BaseExtractor, BaseReader

class OrganizationInfoExtractor(BaseExtractor):
    def __init__(self):
        super().__init__()

    @property
    def FILE_MAP(self):
        FILE_MAP: dict[str, BaseReader] = {
            "xlsx": ExcelAgencyReader(),
            "pdf": PdfAgencyReader()
        }
        return FILE_MAP
