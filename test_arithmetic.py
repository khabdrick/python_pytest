# test_arithmetic.py

import arithmetic

def test_sum():
    assert arithmetic.sum(5, 2)== 7
    assert arithmetic.sum(100, 200)==300
    assert type(arithmetic.sum("Hi ", "there")) is str 
    assert arithmetic.sum("Hi ", "there") == "Hi there"

def test_minus():
    assert arithmetic.minus(5, 2) >= 2
    assert arithmetic.minus(-5, -5)==0