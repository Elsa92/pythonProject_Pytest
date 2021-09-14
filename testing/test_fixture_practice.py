import pytest
import yaml


# def add(a,b):
#     return a+b
from pythoncode.calculator import Calculator


#获取数据
def get_data():
    with open('../datas/calc.yml','rb') as f:
        total = yaml.safe_load(f)
        return total['datas'], total['ids']

#检测获取的数据
# def test_data():
#     print(get_data())

# request.param 实现了数据的获取
# ids 为每条数据起个别名，fixture实现
@pytest.fixture(params=get_data()[0] , ids=get_data()[1])
def get_datas(request):
    return request.param



class TestDemo:

    # def setup_class(self):
    #     self.calc = Calculator()
    #     print('开始计算')
    #
    # def teardown_class(self):
    #     print('结束计算')

    # @pytest.mark.parametrize('a,b,expect',get_data()[0],ids = get_data()[1])
    def test_add_1(self,get_calc,get_datas):
        assert get_datas[2] == get_calc.add(get_datas[0],get_datas[1])