'''
    获取当前activity
        adb logcat| grep ActivityManager
        adb shell dumpsys  activity activities
'''

#encoding = utf-8

from appium import webdriver
caps = {};
caps["platformName"] = "android"
caps["deviceName"] = "demo"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
# 添加去掉权限弹窗
caps["autoGrantPermissions"] = "true"
caps["automationName"] = "uiautomator2"

#获取驱动
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

driver.find_element_by_id("user_profile_icon").click()

# driver.quit()












