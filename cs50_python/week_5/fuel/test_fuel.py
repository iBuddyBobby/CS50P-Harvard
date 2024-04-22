from fuel import gauge, convert
import pytest

def test_wrong_fraction():
    with pytest.raises(ValueError):
        convert("4/3")
        convert("2/1")
        convert("101/100")

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/3") == 33
    assert convert("1/100") == 1
    assert convert("1/2") == 50
    assert convert("3/4") == 75

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
