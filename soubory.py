from pathlib import Path

#1
def otevreni_souboru(file_path):
    path_to_file = Path.open(file_path)
    file_content = path_to_file.read()
    return file_content

file_path = input("Full path of the file: ")
file_content_path = input("Full path of the content of the file: ")
file_content = Path(file_content_path).open("w")
file_content.write(otevreni_souboru(file_path))

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

read_and_write_passwd()
check_directory()