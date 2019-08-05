from selenium.webdriver.common.by import By

from pageobject.page.BasePage import BasePage
from pageobject.page.LoginPage import LoginPage


class ProfilePage(BasePage):
    def gotoLogin(self):
        self.loadsteps("../data/ProfilePage.yaml", "gotoLogin")
        return LoginPage()