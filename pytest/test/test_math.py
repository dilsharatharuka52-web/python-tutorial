import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_tow():
    a = 1
    b = 2
    c = 3
    assert a + b == c


# def test_divide_by_zero():
#     try:
#         num = 1 / 0
#         assert num
#     except ZeroDivisionError as e:
#         print(e)    

# Exception Testing 
# We are testing whether Python raises a ZeroDivisionError when we try to divide a number by zero.

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1  / 0

    assert 'division by zero' in str(e.value)


# Parameterizinf test cases

product = [
  (2, 3, 6),
  (1, 99, 99),
  (0, 99, 0),
  (3, -4, -12),
  (-5, -5, 25),
  (2.5, 6.7, 16.75)
]

@pytest.mark.parametrize('a, b, product', product)
def test_multiplication(a, b, product):
    assert a * b == product

# Api maka normal karna widhihata korath aka line akak brake unata
# pasa eta yatin tiyana okoma brake wanwa aka nisa maka use karanawa

# Testing class and method

numbers = [
    (10, 10),
    (-10, 10),
    (3.14, 3.14),
    (-3.14, 3.14)
]

@pytest.mark.parametrize('numbr, answer', numbers)
def test_absolute_value(numbr, answer):
    assert abs(numbr) == answer