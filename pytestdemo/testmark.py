import pytest

class TestClass:
    @pytest.mark.runtest
    def test_run(self):
        print("run................")

    @pytest.mark.notruntest
    def test_not_run(self):
        print("not run !!!!!!!!!!!!")

'''
    命令行执行：
        pytest -s testmark.py -m=runtest    -s 指定要执行的文件，-m要执行的标记
        pytest -s testmark.py -m "not runtest"   not runbtest  表示除runtest外的都执行
'''

