# data_ingestion.py

def read_file(path):
    """
    Read a text file and return its content as a string.
    Returns empty string if file is not found.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return ""