class FileNameException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class ExtractorFileTypeException(Exception):
    def __init__(self, file_extension: str, obj_name: str):
        self.message = f"File type '.{file_extension}' is not a valid file type for Extractor '{obj_name}'"

    def __str__(self):
        return self.message
