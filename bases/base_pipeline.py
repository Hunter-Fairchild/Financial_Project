import pandas as pd
from utils.file_selector import file_selector
from bases.base_extractor import BaseExtractor
from abc import ABC, abstractmethod

class BasePipeline(ABC):
    def __init__(self, file_paths: list[str] = None):
        self.file_paths = file_paths if file_paths is not None else file_selector()
    
    def print_progress(self, file_name: str, index: int, length: int, df: pd.DataFrame=None):
        string = f"({index+1} - {length}) Pipeline on '{file_name}'"
        if df is not None:
            string += f"\n{df.head(10).to_string()}"
        print(string)

    @property
    @abstractmethod
    def extractor(self) -> BaseExtractor:
        pass