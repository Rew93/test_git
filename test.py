import pytest


def ispositive(a):
    return True if a > 0 else False


def test_is_positive():
    assert ispositive(4) == True
    assert ispositive(-1) == False

class TestFunc:
    def test_if_positive_number(self):
        assert ispositive(4) == True
        assert ispositive(-1) == False
        assert ispositive(0) == False
