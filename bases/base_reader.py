from abc import ABC, abstractmethod

class BaseReader(ABC):
    @abstractmethod
    def read_file(self, file_path: str):
        pass

