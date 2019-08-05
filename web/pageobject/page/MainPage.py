from selenium.webdriver.common.by import By
from web.pageobject.page.BasePage import BasePage
from web.pageobject.page.TopicPage import TopicPage

class MainPage(BasePage):
    topic_edit = (By.CSS_SELECTOR, ".medium-editor-element", 0)
    def gototopic(self):
        self.find(self.topic_edit).click()
        return TopicPage()
