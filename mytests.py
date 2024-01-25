import mycode

def test_mean1():
    assert mycode.calculate_the_mean([2,4])  == 3


def test_mean2():
    assert mycode.calculate_the_mean([1,5,4,6])  == 4


def test_min():
    assert mycode.get_the_min([2,3,10,3,1]) == 1

def test_max():
    assert mycode.get_the_max([2,3,10,3,1]) == 10



