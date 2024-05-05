
def ReadFromFile(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File:", file_path, "did not exist")
    except Exception as e:
        print("Error occured while reading file:", str(e))


def SaveToFile(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)
        print("File saved succesfully")
    except Exception as e:
        print("Error occured while saving file:", str(e))
