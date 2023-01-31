def is_even_number(a):
    return True if a % 2 == 0 and a != 0 else False


def is_noteven_number(a):
    return True if a % 2 != 0 and a != 0 else False


def is_float_number(a):
    return True if type(a) == float else False

#test case
class TestCase:

    def test_is_even_number(self):
        assert is_even_number(2) == True
        assert is_even_number(1) == False
        assert is_even_number(0) == False

    def test_is_noteven_number(self):
        assert is_noteven_number(2) == False
        assert is_noteven_number(0) == False
        assert is_noteven_number(1) == True

    def test_is_float_number(self):
        assert is_float_number(0.3) == True
        assert is_float_number(1) == False
        assert is_float_number(1.0) == True
        assert is_float_number(-0.1772323) == True
        assert is_float_number(-1) == False
