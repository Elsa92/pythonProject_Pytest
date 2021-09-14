import pytest


@pytest.fixture(scope='module',autouse=True)
def login():
    print('login')
    yield 'Token=12345'
    print ('logout')

# 测试步骤 连接数据库
@pytest.fixture()
def connectDB():
    print('connectDB')
    return 'database---datas'

@pytest.mark.run(order = 3)
def test_case1(login):
     print(login)
     print('case1')

@pytest.mark.run(order = 1)
def test_case2():
    print('case2')

@pytest.mark.run(order = 2)
def test_case3():
    print('case3')