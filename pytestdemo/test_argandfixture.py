import pytest

test_user = ["zs","ls"]

@pytest.fixture()
def login_user(request):
    print(request)
    return request

@pytest.mark.parametrize("login_user",test_user,indirect=True)
def test_001(login_user):
    a = login_user.param
    print("test_001: " + a)



