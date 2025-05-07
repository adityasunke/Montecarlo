import pytest
import numpy as np
from molecool.bitstring import BitString

def test_init_and_len():
    b = BitString(5)
    assert len(b) == 5
    assert all(b.config == np.zeros(5, dtype=int))

def test_repr():
    b = BitString(4)
    assert repr(b) == "0000"
    b.set_config([1, 0, 1, 1])
    assert repr(b) == "1011"

def test_eq():
    b1 = BitString(3)
    b2 = BitString(3)
    assert b1 == b2
    b2.set_config([1, 0, 0])
    assert b1 != b2

def test_on_off():
    b = BitString(4)
    b.set_config([1, 0, 1, 1])
    assert b.on() == 3
    assert b.off() == 1

def test_flip_site():
    b = BitString(3)
    b.set_config([0, 0, 1])
    b.flip_site(0)
    assert list(b.config) == [1, 0, 1]
    b.flip_site(2)
    assert list(b.config) == [1, 0, 0]

def test_integer():
    b = BitString(4)
    b.set_config([1, 0, 1, 1])  # binary 1011 = 11
    assert b.integer() == 11
    b.set_config([1, 1, 1, 1])  # binary 1111 = 15
    assert b.integer() == 15

def test_set_integer_config():
    b = BitString(4)
    b.set_integer_config(11)  # binary 1011
    assert list(b.config) == [1, 0, 1, 1]
    b.set_integer_config(15)  # binary 1111
    assert list(b.config) == [1, 1, 1, 1]

def test_set_config():
    b = BitString(3)
    b.set_config([1, 1, 0])
    assert list(b.config) == [1, 1, 0]
