

# This is the code of data ingestion where we can import the data
def openfile(path):
    with open(path, "r") as file:
        content = file.read()
    return content


# Replace path with your own txt file
content = openfile('../test.txt')
print(content)