import pytest


@pytest.fixture
def number_pair_data():
    return 1, 2


@pytest.fixture(
    params=[(1, 2), (1, 1.5), (2, 0)], scope='session')
def number_pair_datum(request: pytest.FixtureRequest):
    return request.param
