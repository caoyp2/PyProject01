#批量行所有以test_开头的测试方法
#执行顺序是命名顺序：先执行test_case1，再执行test_case2
import  unittest
class Test03:

    def runcases(self):
        #批量行所有以test_开头的测试方法
        discover = unittest.defaultTestLoader.discover("./",pattern='unittestdemo02.py')
        runner = unittest.TextTestRunner()
        runner.run(discover)

test = Test03()
test.runcases()


