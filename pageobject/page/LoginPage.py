from selenium.webdriver.common.by import By
from pageobject.page.BasePage import BasePage


class LoginPage(BasePage):
    _close_locator = (By.ID, "iv_close")
    _other_locator = (By.ID, "tv_login_by_phone_or_others")
    _register_phone_number = (By.ID, "register_phone_number")
    _register_code = (By.ID, "register_code")
    _button_next = (By.ID, "button_next")
    _tv_login_with_account = (By.ID, "tv_login_with_account")
    _login_account = (By.ID, "login_account")
    _login_password = (By.ID, "login_password")
    _close2_locator = (By.ID, "iv_action_back")
    _error_msg = (By.ID, "md_content")
    _back_locator = (By.XPATH, "//*[contains(@resource-id, 'iv_close') or contains(@resource-id, 'iv_action_back')]")

    def loginByPassword(self, account, password):
        #点击账号及其他方式登录
        self.loadsteps("../data/LoginPage.yaml", "loginByPassword", var1=account, var2=password)
        return self

    #登录成功
    def loginSuccessByPassword(self, account, password):
        from pageobject.page.MainPage import MainPage
        return MainPage()

    #点击返回按钮
    def back(self):
        self.find(self._back_locator).click()
        #WebDriverWait(self.driver, 2).until(expected_conditions.presence_of_element_located(self._close_locator))
        from pageobject.page.ProfilePage import ProfilePage
        return ProfilePage()

    #获取msg的方法
    def getErrorMsg(self):
        msg=self.find(self._error_msg).text
        print(msg)
        #点击返回按钮
        self.driver.back()
        return msg