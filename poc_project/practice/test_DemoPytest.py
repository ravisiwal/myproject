import pytest

@pytest.mark.skip
def test_firstprogram():
    print('First pytest program')


@pytest.mark.smoke
def test_secondprogram():
    a= 7
    b=8
    assert a+b == 15, 'addition should match'
    assert a+7 == 12, 'addition should match'

@pytest.mark.xfail
def test_check_program():
    a= 'Ravi'
    b = 'Sharma'
    assert b == 'sharma'


