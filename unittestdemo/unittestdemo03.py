import unittest
from unittestdemo.unittestdemo02 import Test02


class TestSuitDemo:

    def runsuit(self):
        # 实例化测试套件
        suit = unittest.TestSuite()
        suit.addTest(Test02('test_case02'))
        suit.addTest(Test02('test_case01'))

        #实例化TextTestRunner类
        runner = unittest.TextTestRunner()
        runner.run(suit)

testsuit = TestSuitDemo()
testsuit.runsuit()
