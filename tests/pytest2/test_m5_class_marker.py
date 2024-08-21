import pytest

from pytest2 import m5_class_marker as m5


@pytest.fixture
def hoge2() -> m5.Hoge2:
    return m5.Hoge2(1)


@pytest.mark.hoge2
class TestHoge2:
    def test_print(self, hoge2:m5.Hoge2):
        hoge2.print()


@pytest.fixture
def fuga2() -> m5.Fuga2:
    return m5.Fuga2(1)


@pytest.mark.fuga2
class TestFuga2:
    def test_print(self, fuga2:m5.Fuga2):
        fuga2.print()

