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
def test_data():
    print(get_data())


class TestDemo:

    # def setup_class(self):
    #     self.calc = Calculator()
    #     print('开始计算')
    #
    # def teardown_class(self):
    #     print('结束计算')

    @pytest.mark.parametrize('a,b,expect',get_data()[0],ids = get_data()[1])
    def test_add_1(self,get_calc,a,b,expect):
        assert expect == get_calc.add(a,b)