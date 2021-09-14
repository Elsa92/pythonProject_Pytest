import pytest

def func(x):
    return x + 1

def test_anwser():
    assert func(4) == 5

@pytest.mark.parametrize('a,b',[
    (10,20),
    (10,30)
])

def test_add(a,b):
    print(f'{a}+{b}={a+b}')

if __name__ == '__main__':
    pytest.main(['test_b.py'])