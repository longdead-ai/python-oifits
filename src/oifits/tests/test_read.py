import numpy as np

from oifits.data import Data
from oifits.read import OIParser


def test_data_works_fine():
    a = OIParser.read("src/oifits/tests/test.oifits")
    assert isinstance(a.data, Data)
    assert a.t3data == None


def test_export_to_numpy_works_fine():
    a = OIParser.read("src/oifits/tests/test.oifits")
    m = a.export_to_ascii()
    assert isinstance(m, np.ndarray)
