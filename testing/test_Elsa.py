import pytest

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





# if __name__ == '__main__':
#     pytest.main()