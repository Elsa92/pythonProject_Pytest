from decimal import Decimal

import pytest
import yaml


from pythoncode.calculator import Calculator

# def get_calc_data():
#     with open('../datas/calc.yml') as f:
#         total = yaml.safe_load(f)
#         return total['datas'], total['ids']
#
# def test_get_data():
#     print(get_calc_data())

def get_calc_data():
    with open('../datas/calc.yml','rb') as f:
        total = yaml.safe_load(f)
        add_success_datas = total['add']['add_success']['datas']
        add_success_ids = total['add']['add_success']['ids']
        add_fail_datas = total['add']['add_fail']['datas']
        add_fail_ids = total['add']['add_fail']['ids']
        div_success_datas = total['div']['div_success']['datas']
        div_success_ids = total['div']['div_success']['ids']
        div_fail_datas = total['div']['div_fail']['datas']
        div_fail_ids = total['div']['div_fail']['ids']

        return add_success_datas, add_success_ids,add_fail_datas,add_fail_ids,div_success_datas,div_success_ids,div_fail_datas,div_fail_ids

# def test_getdatas():
#     print(get_calc_data())

class TestCalculator:

    def setup_class(self):
        self.calculator = Calculator()
        print('开始计算')
    def teardown_class(self):
        print('结束计算')

    '''
    测试加法正常场景
    整数相加
    浮点数相加
    '''
    @pytest.mark.parametrize('a,b,expect',get_calc_data()[0],ids = get_calc_data()[1])
    def test_add_success(self,a,b,expect):

        if type(a) and type(b) is float:
            # a = Decimal(a)
            # b = Decimal(b)
            # assert expect == self.calculator.add(a,b)
            assert expect == round(self.calculator.add(a,b),2)
        else:
            assert expect == self.calculator.add(a,b)
    '''
    测试加法异常场景
    '''
    @pytest.mark.parametrize('a,b',get_calc_data()[2], ids = get_calc_data()[3])
    def test_add_fail(self,a,b,):
        with pytest.raises(ValueError) as e:
            self.calculator.add(float(a),float(b))
            assert e.type == ValueError

    '''
    测试除法正常场景
    '''
    @pytest.mark.parametrize('a,b,expect',get_calc_data()[4], ids = get_calc_data()[5])
    def test_div_success(self,a,b,expect):
            assert expect == self.calculator.div(a,b)
    '''
    测试除法异常处理
    '''
    @pytest.mark.parametrize('a,b',get_calc_data()[6], ids = get_calc_data()[7])
    def test_div_fail(self, a,b):
        if b==0:
            with pytest.raises(ZeroDivisionError) as e:
                self.calculator.div(a,b)
                assert e.type == ZeroDivisionError
        else:
            with pytest.raises(TypeError) as e:
                self.calculator.div(a,b)
                assert e.type == TypeError


