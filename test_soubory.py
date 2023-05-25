import pytest
import soubory as s
from pathlib import Path

@pytest.mark.parametrize(
        "command,expected",
        [
            ("/tmp/passwd.txt", "Username")
        ]
    )

def test_red_and_write_passwd(command, expected):
    #print(s.Soubory.read_and_write_passwd(command), expected)
    s.Soubory.read_and_write_passwd(command)
    path = Path(command).open("r")
    print(path)
    lines = path.read()
    path.close()
    assert expected in lines

@pytest.mark.parametrize(
        "command,expected",
        [
            ("/tmp/", True),
            ("/usr/bin/", True),
            ("/RandomDir", False)
        ]
    )

def test_check_directory(command, expected):
    assert s.Soubory.check_directory(command) == expected
