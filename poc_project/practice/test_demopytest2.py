import pytest

@pytest.fixture()
def myfixture():
    print('This will execute first')
    yield
    print("This will execute after test executed")

def test_my_function(myfixture):
    print("This will execute after fixture")





