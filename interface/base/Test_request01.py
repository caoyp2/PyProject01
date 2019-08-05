import logging
import requests
import json
import jsonpath
from hamcrest import *
from jsonschema import validate
class Test_request01(object):
    logging.basicConfig(level=logging.INFO)
    def test_01(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        logging.info(r)
        logging.info(r.text)
        # indent 代表缩进     separators 表示以什么进行分隔
        logging.info(json.dumps(r.json(),indent=2, separators=(',', ': ')))

    def test_02(self):
        r = requests.post("http://testerhome.com/api/v3/topics.json?limit=2",
                         json={"a":1,"b":2},     #添加请求参数
                         headers={"a":"a","b":"b"},  #添加header内容
                         proxies={"http":"http://127.0.0.1:8888",
                                  "https":"http://127.0.0.1:8888"}, #启用代理
                         verify=False #不验证
                        )
        logging.info(r)
        logging.info(r.text)
        
    def test_03(self):
        cookies = {"xq_a_token":"5806a70c6bc5d5fb2b00978aeb1895532fffe502","u":"3446260779"}
        headers = {"User-Agent":"Xueqiu Android 11.19","Accept-Language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4","Host":"stock.xueqiu.com"}
        params = {"t":"1UNKNOWNc60715cb4a61425b311034a49f4aa024.3446260779.1563002521424.1563005246620",
                  "_s":"8c6b2d",
                  "category":"1",
                  "pid":"-1",
                  "size":"10000",
                  "x":"1.3",
                  "page":"1"
                  }
        r = requests.get("https://101.201.175.228/v5/stock/portfolio/stock/list.json",
                         params=params,
                         cookies=cookies,
                         headers=headers,
                         verify=False
                         )
        logging.info(json.dumps(r.json(),indent=2))

    def test_hamcrest(self):
        cookies = {"xq_a_token": "5806a70c6bc5d5fb2b00978aeb1895532fffe502", "u": "3446260779"}
        headers = {"User-Agent": "Xueqiu Android 11.19", "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
                   "Host": "stock.xueqiu.com"}
        params = {"t": "1UNKNOWNc60715cb4a61425b311034a49f4aa024.3446260779.1563002521424.1563005246620",
                  "_s": "8c6b2d",
                  "category": "1",
                  "pid": "-1",
                  "size": "10000",
                  "x": "1.3",
                  "page": "1"
                  }
        r = requests.get("https://101.201.175.228/v5/stock/portfolio/stock/list.json",
                         params=params,
                         cookies=cookies,
                         headers=headers,
                         verify=False
                         )
        assert_that(jsonpath.jsonpath(r.json(),"$.data.stocks[*].name"),
                    any_of(has_item('招商银行'),has_item('平安银行')))


    def test_hamcrest01(self):
            assert_that(["a","b","c"],has_items("a","d"))


    def test_jsonschema(self):
        schema = {
        "type": "object",
        "properties":
            {
                "price": {"type": "number"},
                "name": {"type": "string"},
            },
        }
        validate(instance={"name": "Eggs", "price": "34.99"}, schema=schema)

