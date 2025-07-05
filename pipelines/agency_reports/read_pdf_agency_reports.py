import pandas as pd
import pypdf
import re

from bases.base_reader import BaseReader
from bases.typed_dicts import AccountDict

class PdfAgencyReader(BaseReader):
    def __init__(self):
        self.account_pattern = r"\d\d-\d\d-\d{5}.* - .* [0-9,.()]* [0-9,.()]* [0-9,.()]*"

    def read_file(self, file_path: str) -> pd.DataFrame:
        """Reads PDF file version of agency accounts report and transforms content into a formatted version. 

        Args:
            file_path (str): File path of pdf file of agency accounts report

        Returns:
            pd.DataFrame: Formatted dataframe of pdf content
        """
        reader = pypdf.PdfReader(file_path)
        pages = [page.extract_text() for page in reader.pages]

        accounts = []

        for page in pages:
            accounts += self.read_page(page)

        df = pd.DataFrame(accounts)

        return df

    def read_page(self, page: str) -> list[AccountDict]:
        """Reads pdf page and outputs a list of typed dictionaries of accounts

        Args:
            page (str): page contents

        Returns:
            list[AccountDict]: list of typed dictionaries for each account
        """
        accounts = re.findall(self.account_pattern, page)

        accounts = [
            self.read_account(account) for account in accounts
        ]
        return accounts

    def read_account(self, account_str: str) -> AccountDict:
        """Reads account string and structures it into a typed dictionary for use in python. 

        Args:
            account_str (str): String version as read from pdf of account line

        Returns:
            AccountDict: Dict version of line of account from pdf
        """
        account_list, opening, activity, ending_balance = account_str.rsplit(maxsplit=3)
        no, name = account_list.split(" ", maxsplit=1)

        formatted_account: AccountDict = {
            "account_number": no,
            "account_name": name,
            "opening_balance": opening,
            "cactivity": activity,
            "ending_balance": ending_balance,
        }
        assert no.count("-") == 2 and len(no)==11
        return formatted_account


if __name__ == "__main__":
    path = "E:\\Projects\\SGA_Financial_Reporting\\data\\raw_balance_reports\\Agency Account Report 24-06-10.pdf"
    p = PdfAgencyReader()
    print(p.read_file(path))
