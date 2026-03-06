
# This is the code of data ingestion where we can import the data
def openfile(path):
    with open(path, "r") as file:
        content = file.read()
    return content

