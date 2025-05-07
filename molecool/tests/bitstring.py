import pytest
from molecool.bitstring import BitString

def test_init():
    bs = BitString(5)
    assert len(bs.config) == 5

def test_flip_site():
    bs = BitString(3)
    bs.flip_site(1)
    assert bs.config[1] == 1

def test_on_off_counts():
    bs = BitString(2)
    bs.flip_site(0)
    assert bs.on() == 1
    assert bs.off() == 1
