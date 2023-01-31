def ispositive(a):
    return True if a > 0 else False

def isnatural(a):
    return True if a == int(a) and a >= 0 else False

def isnegative(a):
    return True if a <= 0 else False


class TestFunc:
    def test_ispositive_number(self):
        assert ispositive(4) == True
        assert ispositive(-1) == False
        assert ispositive(0) == False

    def test_isnatural(self):
        assert isnatural(0.3) == False
        assert isnatural(-1) == False
        assert isnatural(0) == True
        assert isnatural(1) == True
    
    def test_isnegative_number(self):
        assert isnegative(-10) == True
        assert isnegative(0) == True
        assert isnegative(1) == False
