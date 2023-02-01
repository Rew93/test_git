# This test to random my func

def take_number(a, b):
    return 'Your win' if a == b else 'Your lose'


class TestTakeNumber:

    def test_your_win(self):
        assert take_number(1, 1) == 'Your win'

    def test_your_lose(self):
        assert take_number(0, 10) == 'Your lose'
