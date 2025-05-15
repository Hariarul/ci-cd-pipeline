# tests/test_main.py
from src.main import add

def test_add():
    assert add(1, 3) == 4
    assert add(0, 0) == 0
    assert add(4, 1) == 5
