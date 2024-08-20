import pytest

from pytest2 import module1


def test_print_name():
    module1.print_name()


def test_div():
    module1.div(1, 2)


def test_div_v2():
    module1.div(1, 2)
    module1.div(2, 1)
    module1.div(1.5, 2)
    module1.div(2, 1.5)
    with pytest.raises(ZeroDivisionError) as e:
        module1.div(1, 0)


@pytest.mark.parametrize(
    "x1, x2", [(1, 2), (2, 1), (1.5, 2), (2, 1.5), (0, 1), (1, 0)]
)
def test_div_v3(x1, x2):
    if x2 != 0:
        module1.div(x1, x2)
    else:
        with pytest.raises(ZeroDivisionError) as e:
            module1.div(x1, x2)


def test_div_v4(number_pair_data):
    x1 = number_pair_data[0]
    x2 = number_pair_data[1]
    module1.div(x1, x2)