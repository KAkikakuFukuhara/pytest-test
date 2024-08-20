import pytest

from pytest2 import module2

@pytest.fixture
def add_pair_data():
    return 1, 2


def test_add(add_pair_data):
    x1 = add_pair_data[0]
    x2 = add_pair_data[1]
    module2.add(x1, x2)


def test_add_v2(number_pair_data):
    x1 = number_pair_data[0]
    x2 = number_pair_data[1]
    module2.add(x1, x2)


def test_add_v3(number_pair_datum):
    x1 = number_pair_datum[0]
    x2 = number_pair_datum[1]
    module2.add(x1, x2)
