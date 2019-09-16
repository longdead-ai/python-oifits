import numpy as np

from oifits.utils import _angpoint, _array_eq, _plurals


def test_plural():
    m = 5
    p = 1
    assert _plurals(m) == "s"
    assert _plurals(p) == ""


def test_array_eq():
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    assert _array_eq(a, b)


def test_angpoint_eq():
    a = _angpoint(12.5)
    b = _angpoint(12.5)
    assert a == b


def test_angpoint_asdms():
    b = _angpoint(12.5)
    m = (12.0, 30.0, 0.0)
    assert m == b.asdms()


def test_angpoint_ashms():
    b = _angpoint(12.5)
    m = (0.0, 50.0, 0.0)
    assert m == b.ashms()


def test_angpoint_as_integer_ration():
    b = _angpoint(12.5)
    m = (25, 2)
    assert m == b.as_integer_ratio()
