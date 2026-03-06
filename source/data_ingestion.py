# data_ingestion.py

def read_file(path):
    """
    Read text file and return content as string.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return ""