import math_func
import pytest


@pytest.mark.parametrize('num1, num2, result', [(5, 6, 11), ('Hello', ' World',  'Hello World'), (10.5, 11.7, 22.2)])
def test_add(num1, num2, result ):
    assert math_func.add(num1, num2) == result


@pytest.mark.skip(reason = "do not run this test")
def test_add_num():
    assert math_func.add(5,6) ==11
    assert math_func.add(8) == 12

def test_product():
    assert math_func.product(4,9) == 36
    assert math_func.product(6) == 12
    assert math_func.product(8,3) == 24


@pytest.mark.BQ
def test_add_strings():
    result = math_func.add('Hello', ' world')
    assert result == 'Hello world'
    assert type(result) is str
    assert 'deldo' not in result


def test_product_string():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert 'Hello' in result
