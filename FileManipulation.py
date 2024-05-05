
def ReadFromFile():
    file_path = "text.txt"

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Zawartość pliku:")
            return content
    except FileNotFoundError:
        print("Plik", file_path, "nie istnieje.")
    except Exception as e:
        print("Wystąpił błąd podczas wczytywania pliku:", str(e))
