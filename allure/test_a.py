import pytest


def func(x):
    return x + 1


@pytest.mark.parametrize('a,b',[
                             (1, 2),
                             (3, 4),

                         ])
def test_answer(a, b):
    assert func(a) == b


def test_anwser1():
    assert func(4) == 5

@pytest.fixture()
def login():
    print('登录操作')
    username = 'Elsa'
    return username

class TestDemo():

    def test_a(self, login):
        print(f'this is a,  username={login}')


    def test_b(self):
        print('this is b')


if __name__ == '__main__':
    pytest.main(['test_a.py'])
