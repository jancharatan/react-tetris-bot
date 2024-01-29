import pytest

@pytest.fixture
def square_tile():
    return [
        ["c", "c", "", ""],
        ["c", "c", "", ""]
    ]

@pytest.fixture
def t_tile():
    return [
        ["", "c", "", ""],
        ["c", "c", "c", ""]
    ]