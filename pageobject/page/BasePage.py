from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import yaml
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.driver.Client import Client

class BasePage(object):
    def __init__(self):
        self.driver = Client.driver

    def find(self,kv) -> WebElement:
        #加智能等待
        
        return self.driver.find_element(*kv)


    def findByText(self,text):
        return self.find((By.XPATH,"//*[text='%s']" %text))

    def loadsteps(self,po_path, key, **kwargs):
        file = open(po_path,"r")
        #加载yaml文件类容
        po_data = yaml.load(file)
        #获取yaml文件中指定key的字典内容
        po_method = po_data[key]
        element_platform = dict()
        for step in po_method:
            if step.__contains__("element"):
                element_platform = po_data["elements"][step["element"]][Client.platform]
            else:
                element_platform={"by": step['by'], "locator": step['locator']}
            element: WebElement = self.find(by=element_platform["by"], value=element_platform['locator'])
            action=str(step['action']).lower()
            # todo: 定位失败，多数是弹框，try catch后进入一个弹框处理 元素智能等待
            if action == "click":
                element.click()
            elif action == "sendkeys":
                text = str(step['text'])
                for k, v in kwargs.items():
                    text = text.replace("$%s" % k, v)
                    print("update text: %s" % (text))
                element.send_keys(text)
            else:
                print("UNKNOW COMMAND %s" % step)


    def wait_element(self,time,locator,locator_value,msg):

        WebDriverWait(self.driver,time)\
            .until(expected_conditions.presence_of_element_located((locator,locator_value)),msg)