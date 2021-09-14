
# 测试步骤 登录
import pytest


@pytest.fixture()
def login():
    print('login')
    return 'token'

# 测试步骤 连接数据库
@pytest.fixture()
def connectDB():
    print('connectDB')
    return 'database---datas'

def test_case1(login, connectDB):
     print(f'登录的操作的返回值是：{login}')
     print('case1')

@pytest.mark.usefixtures('login')
def test_case2():
    print('case2')

def test_case3(login):
    print('case3')

