from pageobject.driver.Client import Client
from pageobject.page.MainPage import MainPage


class App(object):
    @classmethod
    def main(cls):
        Client.restart_app()
        #启动app后返回一个主页面
        return MainPage()