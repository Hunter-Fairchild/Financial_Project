from abc import ABC, abstractmethod
from bases.base_reader import BaseReader
from utils.exceptions import ExtractorFileTypeException


class BaseExtractor(ABC):
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

    def get_reader(self, file_extension: str) -> BaseReader:
        if file_extension not in self.FILE_MAP.keys():
            raise ExtractorFileTypeException(file_extension, self.__class__.__name__)
        return self.FILE_MAP[file_extension]

