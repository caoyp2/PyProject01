#encoding = utf-8
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction



caps = {};
caps["platformName"] = "android"
caps["deviceName"] = "demo"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
# 添加去掉权限弹窗
caps["autoGrantPermissions"] = "true"
#数据不清理，默认为false
# caps["noReset"]=True

#获取驱动
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
ele = driver.find_element_by_xpath("//*[@text='交易']")
index = 0
while True:
    loc1 = ele.location
    print("loc1:" + str(loc1))
    time.sleep(2)
    loc2 = ele.location
    print("loc2:" + str(loc2))
    index = index + 1
    if index > 5:
        break

driver.quit()
