import numpy as np
from molecool.bitstring import BitString

def test_init_and_repr():
    bs = BitString(4)
    assert len(bs) == 4
    assert repr(bs) == "0000"

def test_flip_site():
    bs = BitString(2)
    bs.flip_site(0)
    assert bs.config[0] == 1
    bs.flip_site(0)
    assert bs.config[0] == 0

def test_integer():
    bs = BitString(3)
    bs.set_config(np.array([1, 0, 1]))
    assert bs.integer() == 5

def test_set_config_and_on_off():
    bs = BitString(2)
    bs.set_config(np.array([1, 0]))
    assert bs.on() == 1
    assert bs.off() == 1
