import pytest

test_user=[{"name":"lisi","passwd":"123456"},{"name":"wangwu","passwd":"456789"}]
test_search = [{"search":"百度"},{"search":"谷歌"}]

@pytest.fixture()
def login_user(request):
    name = request.param["name"]
    passwd = request.param["passwd"]

    print(name + "---" + passwd)
    return request.param

@pytest.fixture()
def search_name(request):
    serach = request.param["search"]
    print(serach)
    return request.param


@pytest.mark.parametrize("search_name",test_search,indirect=True)
@pytest.mark.parametrize("login_user",test_user,indirect=True)
def test_001(login_user,search_name):
    print(login_user)
    print(search_name)



