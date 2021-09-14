from time import sleep

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


def test_case1(login):
    sleep(1)
    print(login)
    print('case1')


def test_case2():
    sleep(1)
    print('case2')

def test_case3():
    sleep(1)
    print('case3')

'''
运行命令 pytest - n 3
'''