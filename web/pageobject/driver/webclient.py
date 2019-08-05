import yaml
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver


class webclient(object):

    #启动浏览器
    driver: WebDriver
    browser = "chrome"
    @classmethod
    def startbrowser(cls) -> WebDriver:
        cls.driver = cls.initdriver("startbrowser")
        return cls.driver

    @classmethod
    def initdriver(cls,key) -> WebDriver:
        driver_data = yaml.load(open("../data/webdriver.yaml", "r"))
        browser_run = str(driver_data["browser"]).lower()
        server = driver_data[key]["server"]
        implicitly_wait = driver_data[key]["implicitly_wait"]
        project_adress = driver_data[key]["project_adress"]
        capabilities = {}
        if browser_run == "chrome":
            capabilities = DesiredCapabilities.CHROME
        elif browser_run == "firfox":
            capabilities = DesiredCapabilities.FIREFOX
        else:
            capabilities = DesiredCapabilities.INTERNETEXPLORER

        cls.driver = webdriver.Remote(
            command_executor=server,
            desired_capabilities=capabilities)
        cls.driver.implicitly_wait(implicitly_wait)
        cls.driver.get(project_adress)
        return cls.driver





