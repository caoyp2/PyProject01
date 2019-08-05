
import unittest
class Test02(unittest.TestCase):

    #setUpClass  tearDownClass 类中所有的测试方法运行开始和结束的时候，只执行一次
    @classmethod
    def setUpClass(cls):
        print("登录！！！！")


    def test_case01(self):
        print("添加购物车。。。。")

    def test_case02(self):
        print("结算。。。。。")

    @classmethod
    def tearDownClass(cls):
        print("注销、。。。。。。。。。。")


if __name__ == "__main__":
    unittest.main()