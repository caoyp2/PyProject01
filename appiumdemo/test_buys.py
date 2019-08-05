import time

import pytest
from appium import webdriver

class Testbuys:
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
        element = self.driver.find_element_by_xpath("//*[@text='交易']")
        #判断页面是否已经加载完成
        self.isFixedLocation(element)
        self.driver.find_element_by_xpath("//*[@text='交易']").click()

    @pytest.mark.parametrize("phone,passwd",[("18380461234","123456")])
    def test_buys01(self,phone,passwd):
        element = self.driver.find_element_by_accessibility_id("基金开户")
        self.isFixedLocation(element)
        self.driver.find_element_by_accessibility_id("基金开户").click()


        accele = self.driver.find_element_by_accessibility_id("已有蛋卷基金账户登录")
        self.isFixedLocation(accele)
        self.driver.find_element_by_accessibility_id("已有蛋卷基金账户登录").click()

        self.driver.find_element_by_accessibility_id("使用密码登录").click()
        self.driver.find_element_by_id("telno").send_keys(phone)
        self.driver.find_element_by_id("pass").send_keys(passwd)
        self.driver.find_element_by_id("next").click()
        message = self.driver.find_element_by_id("android:id/message").text
        self.driver.back()
        assert message == "你输入的手机号码或者密码有误"

    def teardown_method(self):
        self.driver.back()
        self.driver.back()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def isFixedLocation(self,element):
        while True:
            loc1 = element.location
            time.sleep(2)
            loc2 = element.location
            if loc1 == loc2:
                print("页面加载完成。。。。。。。")
                break


