
def ReadFromFile(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("Plik", file_path, "nie istnieje")
    except Exception as e:
        print("Wystąpił błąd podczas wczytywania pliku:", str(e))


def SaveToFile(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)
        print("Plik został pomyślnie zapisany")
    except Exception as e:
        print("Wystąpił błąd podczas zapisywania pliku:", str(e))
