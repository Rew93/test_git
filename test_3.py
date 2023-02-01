# This random win or lose

import random

a = int(input())
b = random.randrange(1, 11)


def take_number(a, b):
    return 'Your win' if a == b else 'Your lose'


class TestTakeNumber:

    def test_you_win(self):
        assert take_number(1, 1) == 'Yore win'
        assert take_number(0, 10) == 'Yore lose'
