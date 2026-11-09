import pytest
from stuff.accum import Accumlator


@pytest.fixture
def accum():
    return Accumlator()