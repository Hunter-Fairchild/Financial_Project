import datetime


def get_current_date() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_file_type(file_path: str) -> str:
    return file_path.split(".")[-1]

