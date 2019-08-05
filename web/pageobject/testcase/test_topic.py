from web.pageobject.driver.webclient import webclient
from web.pageobject.page.MainPage import MainPage
from web.pageobject.testcase.BaseTestCase import BaseTestCase


class Test_Topic(BaseTestCase):

    # @classmethod
    # def setup_class(cls):
        #打开雪球
        # webclient.startbrowser()
        # cls.topicpage = MainPage().gototopic()

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_publishtopic(self):
        self.topicpage.publishtopic("发布一个信息")

    def test_log(self):
        self.log.warning("这是一个测试。。。。。")
        self.log.debug("这是一个debug")




