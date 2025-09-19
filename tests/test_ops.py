import math
from calculator import add, sub, mul, div
import pytest

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(10, 4) == 6

def test_mul():
    assert mul(6, 7) == 42

def test_div_basic():
    assert div(9, 3) == 3

def test_div_float():
    assert math.isclose(div(7, 2), 3.5)

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
