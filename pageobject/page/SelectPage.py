from selenium.webdriver.common.by import By

from pageobject.driver.Client import Client
from pageobject.page.BasePage import BasePage


class SelectPage(BasePage):

    def addDefault(self):
        return self

    def getPriceByName(self,name) -> float:
        #todo
        priceloc = (By.XPATH,"//*[contains(@resource-id, 'stockName') and @text='%s']" %name +
             "/../../..//*[contains(@resource-id, 'currentPrice')]")
        price = self.find(priceloc).text
        return float(price)

