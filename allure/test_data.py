import pytest
import yaml

'''

class TestData:

    # @pytest.mark.parametrize(['a','b'],[(10,20),(10,5),(5,14)])
    @pytest.mark.parametrize(('a','b'), yaml.safe_load(open('./data.yaml')))
    def test_data(self,a,b):
        print(a+b)
'''

class TestDemo:

    @pytest.mark.parametrize('env', yaml.safe_load(open('env.yml')))
    def test_demo(self, env):
        if 'test' in env:
            print('这是测试环境')
            # print(env)
            print('测试环境的IP是：', env['test'])
        if 'dev' in env:
            print('这是开发环境')
            print(env['dev'])

