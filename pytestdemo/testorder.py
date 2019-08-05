import pytest

@pytest.mark.run(order=2)
def test_gouwu():
    print("这是购物。。。。。。。")


@pytest.mark.run(order=1)
def test_login():
    print("这是登录。。。。。。。")
    assert 1 == 1