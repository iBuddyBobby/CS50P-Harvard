
from plates import is_valid

def test_correct():
    assert is_valid("CS5000") == True

def test_incorrect():
    assert is_valid("C50000") == False
    assert is_valid("5000") == False
    assert is_valid("CS50000") == False
    assert is_valid("C") == False
    assert is_valid("CC50SS") == False
    assert is_valid("CS055") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS50.") == False
    assert is_valid("CS,50") == False
