from abc import ABC, abstractmethod
import datetime
import re

from bases.base_reader import BaseReader
from utils.exceptions import ExtractorFileTypeException
from utils.exceptions import FileNameException


class BaseExtractor(ABC):
    def __init__(self):
        super().__init__()
        self.date_match_str = r"\d\d.{1}\d\d.{1}\d{2,4}"

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


    def get_reader(self, file_extension: str) -> BaseReader:
        if file_extension not in self.FILE_MAP.keys():
            raise ExtractorFileTypeException(file_extension, self.__class__.__name__)
        return self.FILE_MAP[file_extension]

    @abstractmethod
    def extract_files(self, file_paths: list[str]):
        pass
    
    @abstractmethod
    def extract_file(self, file_path: str):
        pass

    @property
    @abstractmethod
    def FILE_MAP(self) -> dict[str, BaseReader]:
        pass

    

