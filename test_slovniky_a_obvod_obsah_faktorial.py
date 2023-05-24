import pytest
import slovniky_a_obvod_obsah_faktorial as s

@pytest.mark.parametrize(
        "command,expected",
        [
            (4, 16),
            (5, 20),
            (6, 24),
        ]
)

def test_obvod(command, expected):
    assert s.obvod(command) == expected

@pytest.mark.parametrize(
        "command,expected",
        [
            (4, 16),
            (5, 25),
            (6, 36),
        ]
)

def test_obsah(command, expected):
    assert s.obsah(command) == expected

@pytest.mark.parametrize(
        "command,expected",
        [
            (3, 6),
            (4, 24),
            (5, 120),
        ]
)

def test_faktorial(command, expected):
    assert s.faktorial(command) == expected