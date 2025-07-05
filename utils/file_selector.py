from tkinter import Tk
from tkinter.filedialog import askopenfilenames

def file_selector() -> list[str]:
    """Opens up tkinter file selector. 

    Returns:
        list[str]: Returns all filepaths selected.
    """
    Tk().withdraw()
    filenames = askopenfilenames()
    return filenames
