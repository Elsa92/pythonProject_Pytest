import allure
import pytest

from pythoncode.calculator import Calculator

class TestCalculator:
    def setup_class(self):
        print('开始执行')
        self.calc = Calculator()

    def teardown_class(self):
         print('执行结束')

    @pytest.mark.add
    def test_add(self):
        # calc = Calculator()
        assert 2 == self.calc.add(1,1)

    @pytest.mark.add
    def test_add1(self):
        # calc = Calculator()
        assert 3 == self.calc.add(1,2)

    @pytest.mark.sub
    def test_sub(self):
        # calc = Calculator()
        assert 2 == self.calc.sub(1,1)

    @pytest.mark.div
    def test_div(self):
        # calc = Calculator()
        assert 1 == self.calc.div(1,1)
