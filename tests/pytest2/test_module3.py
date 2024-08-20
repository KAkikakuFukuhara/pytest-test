from __future__ import annotations
from typing import Any

import pytest

from pytest2.module3 import Hoge, Fuga


@pytest.fixture
def hoge(number_pair_datum) -> Hoge:
    x1 = number_pair_datum[0]
    x2 = number_pair_datum[1]
    return Hoge(x1, x2)


@pytest.mark.hoge
class TestHoge:
    def test_add(self, hoge:Hoge):
        hoge.add()


    def test_div(self, hoge:Hoge):
        if hoge.y != 0:
            hoge.div()
        else:
            with pytest.raises(ZeroDivisionError) as e:
                hoge.div()


@pytest.fixture
def fuga_and_value(number_pair_datum) -> tuple[Fuga, Any]:
    x1 = number_pair_datum[0]
    x2 = number_pair_datum[1]
    fuga = Fuga(x1)
    return fuga, x2


@pytest.mark.fuga
class TestFuga:
    def test_pow(self, fuga_and_value: tuple[Fuga, Any]):
        fuga = fuga_and_value[0]
        value = fuga_and_value[1]
        fuga.pow(value)
