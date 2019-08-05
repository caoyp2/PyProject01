import pytest

'''
    该文件可以配置公共的代码，然后在其他文件中调用
    文件名称必须为conftest
'''
@pytest.fixture()
def login():
    print("登录。。。。。")



@pytest.fixture(scope="session")
def open_brower(request):
    print("打开浏览器")

    def close_brower():
        print("关闭浏览器")

    #最后执行的方法
    request.addfinalizer(close_brower)


