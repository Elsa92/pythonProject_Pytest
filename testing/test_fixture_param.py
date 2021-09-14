
'''
fixture 实现参数化
类似于参数化的功能， 也可以用ids为测试用例起别名
'''
import pytest

'''
request 是pytest内置的fixture
可以直接拿来使用，为测试用例起别名
'''
@pytest.fixture(params=['Tom','Jerry','Elsa'], ids= ['name1','name2','name3'])
def login(request):
    myparam = request.param
    print(f'用户名：{myparam}')
    yield myparam
    print('登录操作')

def test_case1(login):
    print(login)