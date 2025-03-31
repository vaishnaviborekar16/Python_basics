# Function to add two numbers
def add_numbers(a, b):
  return a + b
import pytest
def test_add_numbers():
  assert add_numbers(-2, 2) == 0
  assert add_numbers(1, 1) == 2
  assert add_numbers(0, 0) == 0
  assert add_numbers(8.5, 2.5) == 11.0