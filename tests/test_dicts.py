import pytest

from utils import dicts


@pytest.fixture
def data():
    return {"vcs": "mercurial"}


@pytest.fixture
def data_1():
    return {}


def test_get_val(data, data_1):
    assert dicts.get_val(data, "vcs") == "mercurial"
    assert dicts.get_val(data, "vcs", "git") == "mercurial"
    assert dicts.get_val(data_1, "vcs", "git") == "git"
    assert dicts.get_val(data_1, "vcs", "bazaar") == "bazaar"
