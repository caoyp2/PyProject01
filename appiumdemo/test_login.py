import pytest
from appium import  webdriver
class Testlogin:
    driver = webdriver
    @classmethod
    def setup_class(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 添加去掉权限弹窗
        caps["autoGrantPermissions"] = "true"
        caps["unicodeKeyboard"] = "true"
        caps["resetKeyboard"] = "true"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

    def setup_method(self):
        self.driver.find_element_by_id("user_profile_icon").click()
        self.driver.find_element_by_id("tv_login").click()

    @pytest.mark.parametrize("phone,code",[("18380461234","1234"),("18380465546","5546")])
    def test_login01(self,phone,code):
        #手机及其他登录
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        self.driver.find_element_by_id("register_phone_number").send_keys(phone)
        self.driver.find_element_by_id("register_code").send_keys(code)
        self.driver.find_element_by_id("button_next").click()
        self.driver.back()

    @pytest.mark.parametrize("phone,passwd", [("18380461234", "123456"), ("18380465546", "554656")])
    def test_login02(self,phone,passwd):
        #账户登录
        self.driver.find_element_by_id("tv_login_with_account").click()
        self.driver.find_element_by_id("login_account").send_keys(phone)
        self.driver.find_element_by_id("login_password").send_keys(passwd)
        self.driver.find_element_by_id("button_next").click()
        self.driver.back()

    def teardown_method(self):
        self.driver.back()
        self.driver.back()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
