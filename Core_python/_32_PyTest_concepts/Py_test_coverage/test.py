from .sample import add, add_only_postive

def test_add():
    assert add(12, 13) == 25

def test_add_only_positive_ok():
    assert add_only_postive(5, 5) == 10


def test_add_only_positive_fail():
    assert add_only_postive(5, -2) is None