'''
yeild 激活teardown操作
'''

import pytest

'''
yeild 激活teardown 操作
1. 如果不加autouse = True, 则需要在需要用的测试用例 将fixture名字递到测试用例
2. 如果要测测试用例用到fixture的返回数据， 一应要在测试用例的参数中，加上fixture的名称
'''
'''
通过命令行参数 --setup-show 分析fixture实现过程
每个fixture其实都会被执行两次，使用了yeild之后，会激活第二次执行的操作， 也就是teardown操作的内容
pytest test_fixture5.py --setup-show
'''
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

def test_case1(login):
     print(login)
     print('case1')

def test_case2():
    print('case2')

def test_case3():
    print('case3')