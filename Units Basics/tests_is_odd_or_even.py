from is_odd_or_even_module import is_odd_or_even


def test_is_odd_or_even_2():
    assert is_odd_or_even(2) == True, "error case: 2"

def test_is_odd_or_even_3():
    assert is_odd_or_even(3) == False, "error case: 3"

def test_is_odd_or_even_21():
    assert is_odd_or_even(21) == False, "error case: 21"

def test_is_odd_or_even_0():
    assert is_odd_or_even(0) == True, "error case: 0"

def test_is_odd_or_even_4():
    assert is_odd_or_even(-4) == True, "error case: -4"
    