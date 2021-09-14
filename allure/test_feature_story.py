import pytest
import allure

@allure.feature('登录模块')
class TestLogin:
    @allure.story('登陆成功')
    @allure.title('登陆成功')
    def test_login_successful(self):
        with allure.step('步骤一：打开应用'):
            print('打开应用')
        with allure.step('进入登录界面'):
            print('登陆界面')
        with allure.step('输入用户名和密码'):
            print('输入用户名和密码')
        print('这是登录：测试用例， 登录成功')
        pass

    @allure.story('登陆失败')
    def test_login_fail_a(self):
        print('这是登录： 测试用例， 登陆失败')
        pass

    @allure.story('用户名缺失')
    @allure.title('用户名缺失')
    def test_login_fail_b(self):
        print('用户名缺失')
        pass

    @allure.story('密码缺失')
    def test_login_fail_c(self):
        with allure.step('点击用户名'):
            print('输入用户名')
        with allure.step('点击密码'):
            print('输入密码')
        with allure.step('点击登陆后，登陆失败'):
            assert '1' == 1
            print('登陆失败')

        pass

if __name__ == '__main__':
    pytest.main()