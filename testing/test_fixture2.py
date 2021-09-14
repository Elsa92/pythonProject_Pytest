

'''
fixture 与参数同时存在的情况
'''

import pytest

@pytest.fixture()
def login():
    print('login')
    return 'Token'

@pytest.mark.parametrize('a,b',[[1,2],[3,4]])
def test_param(a,b,login):
    print(a,b,login)