from pathlib import Path

class Soubory:
    #1
    def open_file(file_path):
        path_to_file = Path.open(file_path)
        file_content = path_to_file.read()
        return file_content

    file_path = input("Full path of the file: ")
    file_content_path = input("Full path of the content of the file: ")
    file_content = Path(file_content_path).open("w")
    file_content.write(open_file(file_path))

    #2
    lines = []
    def read_and_write_passwd():
        passwd_path = input("Full path of the content of the file: ")
        passwd = Path(passwd_path).open("w")
        passwd.write("")
        passwd = Path(passwd_path).open("a")
        file_path = Path.open("/etc/passwd")
        for line in file_path.readlines():
            lines = line.split(":")
            #3
            passwd.write(f"Username: {lines[0]} and bash: {lines[-1]}")

    #4
    def check_directory():
        dir = input("Full path of the directory to show: ")
        directory = Path(dir)
        for file in directory.iterdir():
            if file.is_file():
                print(f"{file} is a file")
            elif file.is_dir():
                print(f"{file} is a directory")
            else:
                print("I don't know what that is")

class Pocitani:
    def __init__(self, parameter):
        self.parametr = parameter
        self.obvod(self.parametr)
        self.obsah(self.parametr)
        self.faktorial(self.parametr)

    def obvod(self, strana_a):
        print(f"Obvod ctverce je: {4*strana_a}")

    def obsah(self, strana_a):
        print(f"Obsah ctverce je: {strana_a**2}")

    def faktorial(self, cislo_na_faktorial):
        faktorial = 1
        for i in range(1, cislo_na_faktorial+1):
            faktorial *= i
        print(f"Faktorial čísla {cislo_na_faktorial} je: {faktorial}")


    slovnik = {}

    pocet_cisel_ve_slovniku = int(input("Kolik čísel ve slovníku: "))
    for i in range(pocet_cisel_ve_slovniku):
        key = input("Key: ")
        value = float(input("Value: "))
        slovnik[key] = value

    soucet = 0
    for key, value in slovnik.items():
        soucet += value
    print(soucet)

parametr = int(input("S jakým číslem chceš počítat: "))
pocet = Pocitani(parametr)

soubor = Soubory()
soubor.check_directory