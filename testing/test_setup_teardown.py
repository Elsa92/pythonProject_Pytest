

'''
模块级： setup_module/teardown_module 在模块始末调用（级别最高）
函数级： setup_function/teardown_function 只对函数用例调用（不在类中）
类级： setup_class/teardown_class 只在类中前后调用一次（在类中）
方法级: setup_method/tesrdown_method 在方法始末调用（在类中）
方法级： setup/teardown 运行在调用方法的前后
'''


def setup_module():
    print('setup module')

def teardown_module():
    print('teardown module')

def setup_function():
    print('setup function')

def teardown_function():
    print('teardown function')




#被测方法
def add(a,b):
    return a+b

#测试方法
def test_add1():
    print('1+1 = 2')
    assert 2 == add(1,1)

def test_add2():
    assert 2 == add(1,5)

def test_add3():
    assert 4 == add(1,5)

def test_add4():
    assert 6 == add(1,5)

def test_5():
    assert 7 ==add(5,6)


class TestCalculator():

    def setup_class(self):
        print('setup class')

    def teardown_class(self):
        print('teardown class')

    def test_add6(self):
        assert 7 == add(3,4)




