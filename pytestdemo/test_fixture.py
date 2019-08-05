import pytest

'''scope属性：
    function ——默认值，每个test都运行标识的方法
    class ——每个class的所有test只运行一次
    module——每个module的所有test只运行一次
    session——每个session只运行一次
    
    autouse属性：
        若所有测试方法都需要执行fixture标记的公共方法，则可以直接用autouse="True"属性，
        则不用再每个测试方法上都去加@pytest.mark.usefixtures("before")这句
'''



# @pytest.fixture(scope="module")
# def before():
#     print("登录。。。。。。")


@pytest.mark.usefixtures("login")
def test_01():
    print("添加购物车。。。。。。")

@pytest.mark.usefixtures("login")
def test_02():
    print("支付。。。。。")

if __name__ == "__main__":
    pytest.main("-v","-s","test_fixture.py")