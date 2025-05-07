import pytest
import numpy as np
from molecool.bitstring import BitString

def test_init_and_len():
    bs = BitString(5)
    assert len(bs) == 5
    assert np.all(bs.config == 0)

def test_repr():
    bs = BitString(4)
    expected = "0000"
    assert repr(bs) == expected
    bs.flip_site(1)
    assert repr(bs) == "0100"

def test_eq():
    bs1 = BitString(3)
    bs2 = BitString(3)
    assert bs1 == bs2
    bs1.flip_site(0)
    assert bs1 != bs2

def test_on_off():
    bs = BitString(3)
    assert bs.on() == 0
    assert bs.off() == 3
    bs.flip_site(0)
    bs.flip_site(1)
    assert bs.on() == 2
    assert bs.off() == 1

def test_flip_site():
    bs = BitString(2)
    bs.flip_site(0)
    assert bs.config[0] == 1
    bs.flip_site(0)
    assert bs.config[0] == 0
    bs.flip_site(1)
    assert bs.config[1] == 1

def test_invalid_flip():
    bs = BitString(2)
    with pytest.raises(IndexError):
        bs.flip_site(5)
