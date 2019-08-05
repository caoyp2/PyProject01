from selenium.webdriver.common.by import By
from web.pageobject.page.BasePage import BasePage

class TopicPage(BasePage):
    topic_edit = (By.CSS_SELECTOR, ".medium-editor-element", 0)
    publish_btn = (By.XPATH,"发布")
    def publishtopic(self,key):
        self.find(self.topic_edit).send_keys(key)
        self.find(self.publish_btn).click()
        return self

