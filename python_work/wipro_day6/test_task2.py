"""Write a pytest test case to check if an exception
   is raised for a function that divides two numbers."""

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

import pytest
from divide import divide

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_normal_division():
    assert divide(4, 2) == 2
    assert divide(-4, 2) == -2
    assert divide(6, -2) == -3
    assert divide(-2, -2) == 1


