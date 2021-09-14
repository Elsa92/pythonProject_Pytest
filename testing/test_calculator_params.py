import pytest
import yaml


def add(a,b):
    return a + b

# @pytest.mark.parametrize('a,b,expect',[
#     [1,2,3],[100,200,300],[300,400,500]
# ])

@pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./testdata.yml')))
def test_add(a,b,expect):
    assert expect == add(a,b)

@pytest.mark.parametrize('a,b',[[1,2,],[2,3]], ids = ['int1','int2'])
def test_1(a,b):
    print(a,b)


@pytest.mark.parametrize('b',[3,4,5])
@pytest.mark.parametrize('a',[1,2,3])

def test_add1(a,b):
    print(a,b)