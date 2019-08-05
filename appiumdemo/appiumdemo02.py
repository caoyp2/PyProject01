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

driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']").click()
time.sleep(1)
listmod = []
modules = driver.find_elements_by_xpath("//*[contains(@resource-id,'indicator')]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
for x in modules:
    listmod.append(x.get_attribute("text"))

#右滑len(modules) - index 次
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
touch = TouchAction(driver)
index = listmod.index("基金")
while True:
    for num in range(5):
        #上滑
        touch.press(x = width * 0.5, y = height * 0.8).move_to(x = width * 0.5, y = height * 0.3).release().perform()
        time.sleep(1)

    #下滑
    for num in range(5):
        touch.press(x=width * 0.5, y=height * 0.3).move_to(x=width * 0.5, y=height * 0.8).release().perform()
        time.sleep(1)

    #右滑
    touch.press(x = width * 0.9, y = height * 0.5).move_to(x = width * 0.1, y = height * 0.5).release().perform()
    time.sleep(1)
    index = index + 1
    if index >= (len(listmod) - 1):
        for num in range(5):
            # 上滑
            touch.press(x=width * 0.5, y=height * 0.8).move_to(x=width * 0.5, y=height * 0.3).release().perform()
            time.sleep(1)
        break
    newmodules = driver.find_elements_by_xpath("//*[contains(@resource-id,'indicator')]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
    for x in modules:
        text = x.get_attribute("text")
        if text not in listmod:
            listmod.append(text)

driver.quit()













