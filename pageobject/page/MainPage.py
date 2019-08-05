from selenium.webdriver.common.by import By
from pageobject.page.BasePage import BasePage
from pageobject.page.ProfilePage import ProfilePage
from pageobject.page.SearchPage import SearchPage
from pageobject.page.SelectPage import SelectPage


class MainPage(BasePage):
    _search_button = (By.ID, "home_search")
    def gotoselected(self):
        #todo
        self.findByText("自选")
        self.findByText("自选").click()
        return SelectPage()

    def gotosearch(self):
        self.find(self._search_button).click()
        return SearchPage()

    def gotoProfile(self):
        self.loadsteps("../data/MainPage.yaml","gotoProfile")
        return ProfilePage()

