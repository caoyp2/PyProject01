import os

import allure
import pytest


@allure.feature("登录")
class TestLogin:

    @allure.story("正确的用户明和密码")
    def test_01(self):
        assert True


    @allure.story("正确的用户名和错误的密码")
    def test_02(self):
        with allure.step("验证用户名"):
            allure.attach("name","张三")
        with allure.step("验证密码"):
            allure.attach("passwd","123456")
            assert True

    @pytest.mark.parametrize("name,passwd",[("lisi","123456"),("wangwu","123456")])
    @allure.story("错误的用户名和错误的密码")
    def test_03(self,name,passwd):
        with allure.step("验证用户名和密码"):
            allure.attach("name",name)
            allure.attach("passwd",passwd)
            allure.attach.file("./pytestallure/test.jpg",attachment_type=allure.attachment_type.JPG)
            assert False

    @pytest.mark.skipif(os.system() == "win32",reason="no run")
    @allure.story("冻结的账户")
    def test_04(self):
        assert True



