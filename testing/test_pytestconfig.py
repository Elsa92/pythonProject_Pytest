import pytest


@pytest.fixture()
def get_ini(pytestconfig):
    markers = pytestconfig.getini('markers')
    print(markers)

def test_pytestconfig(get_ini):
    pass