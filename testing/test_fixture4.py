import pytest


@pytest.fixture(scope='module')
def login():
    print('login')
    return 'Token'

# 测试步骤 连接数据库
@pytest.fixture()
def connectDB():
    print('connectDB')
    return 'database---datas'

def test_case1(login):
     print('case1')

def test_case2(login):
    print('case2')

def test_case3(login):
    print('case3')