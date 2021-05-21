# test_arithmetic.py

import arithmetic

def test_sum():
    assert arithmetic.sum(5, 2)== 7
    assert arithmetic.sum(100, 200)==300

def test_sub():
    assert arithmetic.minus(5, 2)==3
    assert arithmetic.minus(-5, -5)==0