import pytest
from selenium import webdriver

class TestXueqiu(object):

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://xueqiu.com/")
        self.driver.maximize_window()

    @pytest.mark.parametrize("user, pw",[("test01","123456")])
    def test_search(self,user,pw):
        search = self.driver.find_element_by_name("q")
        search.clear()
        search.click()
        search.send_keys("alibaba")
        self.driver.find_element_by_class_name("nav__search__addon").click()
        #先找到整行
        tr = self.driver.find_element_by_xpath("//*[text()='01688']/../../../..")
        #找添加按钮
        tr.find_element_by_class_name("follow__control").click()

        username = self.driver.find_element_by_name("username")
        username.click()
        username.send_keys(user)

        password = self.driver.find_element_by_name("password")
        password.click()
        password.send_keys(pw)

        #点击登录
        self.driver.find_element_by_css_selector(".modal__login__btn").click()

    def test_executescript(self):
        #获取页面所有请求的时间统计
        raw = self.driver.execute_script("return JSON.stringify(window.performance.timing)")
        print(raw)

