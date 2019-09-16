import numpy as np

from oifits.data import Data
from oifits.read import OIParser


def test_data_initiates():
    a = Data()
    assert a.target.size == 0
    assert a.vis.size == 0
    assert a.vis2.size == 0
    assert a.t3.size == 0


def test_eq_data_works_fine():
    a = OIParser.read("src/oifits/tests/test.oifits")
    oidata = a.data
    oidata2 = a.data
    assert oidata == oidata2
    assert not oidata != oidata2


def test_add_data_works():
    a = OIParser.read("src/oifits/tests/test.oifits")
    oidata = a.data
    oidata2 = a.data
    oidata3 = oidata + oidata2
    assert isinstance(oidata3, Data)


def test_isvalid_iscon():
    a = OIParser.read("src/oifits/tests/test.oifits")
    oidata = a.data
    assert oidata.isvalid()
    assert oidata.isconsistent()


def test_info_works():
    a = OIParser.read("src/oifits/tests/test.oifits")
    oidata = a.data
    oidata.info()
    assert True
