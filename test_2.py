def is_even_number(a):
    return True if a % 2 == 0 and a != 0 else False


class TestCase:

    def test_is_even_number(self):
        assert is_even_number(2) == True
        assert is_even_number(1) == False
        assert is_even_number(0) == False
