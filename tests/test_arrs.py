import pytest

from utils import arrs


@pytest.fixture
def list_1():
    return [1, 2, 3]


def test_get(list_1):
    assert arrs.get(list_1, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(list_1):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(list_1, 1) == [2, 3]
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice(list_1) == [1, 2, 3]
