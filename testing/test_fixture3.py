


import pytest
# autouse= True 自动应用， autouse 默认是FALSE
@pytest.fixture()
def other():
    print('other')

@pytest.fixture(autouse=True)
def login(other):
    print('login')
    return other

# 测试步骤 连接数据库
@pytest.fixture()
def connectDB():
    print('connectDB')
    return 'database---datas'

def test_case1(connectDB):
     print('case1')

def test_case2():
    print('case2')

def test_case3():
    print('case3')