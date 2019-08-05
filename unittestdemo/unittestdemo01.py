import unittest

#4.定义测试类，父类为unittest.TestCase。
#可继承unittest.TestCase的方法，如setUp和tearDown方法，不过此方法可以在子类重写，覆盖父类方法。
#可继承unittest.TestCase的各种断言方法。
class Test(unittest.TestCase):

#5.定义setUp()方法用于测试用例执行前的初始化工作。
#注意，所有类中方法的入参为self，定义方法的变量也要“self.变量”
    def setUp(self):
        print("开始。。。。。。。。")
        self.number = 10

#6.定义测试用例，以“test_”开头命名的方法
#注意，方法的入参为self
#可使用unittest.TestCase类下面的各种断言方法用于对测试结果的判断
#可定义多个测试用例
#最重要的就是该部分
    def test_case1(self):
        self.assertEqual(10,10)

    def test_case2(self):
        # self.number为期望值，20为实际值
        self.assertEqual(self.number,20,msg="your input is not 20")

    @unittest.skip('暂时跳过用例3的测试')
    def test_case3(self):
        self.assertEqual(self.number,30,msg='Your input is not 30')

#7.定义tearDown()方法用于测试用例执行之后的善后工作。
#注意，方法的入参为self
    def tearDown(self):
        print("结束。。。。。。。。")

#8如果直接运行该文件(__name__值为__main__),则执行以下语句，常用于测试脚本是否能够正常运行
if __name__=='__main__':
#8.1执行测试用例方案一如下：
#unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
#执行顺序是命名顺序：先执行test_case1，再执行test_case2
    unittest.main()