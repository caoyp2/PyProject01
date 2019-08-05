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

    def test_webview01(self):
        print(self.driver.contexts)
        print(self.driver.current_context)
        #设置上下文
        # self.driver.switch_to.context(self.driver.contexts[1])

        #获取所有的窗口句柄
        # self.driver.window_handles
        # 切换window窗口
        # self.driver.switch_to.window(self.driver.window_handles[1])

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


