
def test_two_01():
    print("test_two_01....")

def test_two_02():
    print("test_two_02....")

def test_two_03():
    print("test_two_03....")
    assert False

class Test_run():

    def test_one_01(self):
        print("test_one_01")
        assert False


    def test_one_02(self):
        print("test_one_02")

    def test_one_03(self):
        print("test_one_03")
        assert False


'''
    pytest -s test_run.py  执行文件中的所有测试方法
    pytest -s test_run.py::Test_run  执行文件中test_run类中的测试方法
    pytest -s test_run.py::Test_run::test_one_01   执行某个特定的测试方法
    pytest -s test_run.py -k "Test_run"   执行文件中test_run类中的测试方法
    pytest -s test_run.py -k "Test_run or test_two_01"  执行文件中Test_run类中的所有测试方法，和test_two_01方法
    
    pytest -s test_run.py -x     -x 遇到报错就停止执行
    pytest -s test_run.py -x  --maxfail=2    报错数目为2个时，再停止执行其他测试方法
'''