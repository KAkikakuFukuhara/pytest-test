import pytest

from pytest2 import module4


@pytest.fixture(
    params=[2, 3, 4, 6, 9, 0, -1]
)
def number(request: pytest.FixtureRequest) -> int:
    return request.param


@pytest.mark.combine
@pytest.mark.order(2)
def test_can_divide_6(number: int):
    can_divide = True if number % 6 == 0 else False
    assert can_divide == module4.can_divide_6(number)


@pytest.mark.unit
@pytest.mark.order(1)
def test_can_divide_2(number: int):
    can_divide = True if number % 2 == 0 else False
    assert can_divide == module4.can_divide_2(number)


@pytest.mark.unit
@pytest.mark.order(1)
def test_can_divide_3(number: int):
    can_divide = True if number % 3 == 0 else False
    assert can_divide == module4.can_divide_3(number)

