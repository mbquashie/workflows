# test_example_functions.py

import pytest
from example_functions import my_adder, my_thermo_stat, have_digits

# Test my_adder function
def test_my_adder():
    assert my_adder(1, 2, 3) == 6
    assert my_adder(0, 0, 0) == 0

# Test my_thermo_stat function
def test_my_thermo_stat():
    assert my_thermo_stat(70, 79) == 'Heat'
    assert my_thermo_stat(83, 75) == 'AC'

# Test have_digits function
def test_have_digits():
    assert have_digits("Hello123") == 1
    assert have_digits("NoDigitsHere") == 0

