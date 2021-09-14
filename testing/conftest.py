from typing import List

import pytest

from pythoncode.calculator import Calculator


@pytest.fixture()
def login():
    print('login')
    return 'token'

# 测试步骤 连接数据库
@pytest.fixture()
def connectDB():
    print('connectDB')
    return 'database---datas'

@pytest.fixture()
def get_calc():
    calc= Calculator()
    print('开始计算')
    yield calc
    print('计算结束')

# 改写 pytest_collection_modifyitems hook函数
# 收集上来所有的测试用例之后，修改item的方法
# 一般来说hook会放在conftest.py文件中

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        # item.name  测试用例的名字
        # item.nodeid 测试用例的路径
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
