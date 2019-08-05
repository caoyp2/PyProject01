from selenium.webdriver.remote.webelement import WebElement

from web.pageobject.driver.webclient import webclient


class BasePage(object):
    def __init__(self):
        self.driver = webclient.driver

    def find(self,kv) -> WebElement:
        webelement: WebElement
        if len(kv) > 2 :
            locator = kv[0:2]
            index = int(kv[2])
            webelement = self.driver.find_elements(*locator)[index]
        else:
            webelement = self.driver.find_element(*kv)
        return webelement


