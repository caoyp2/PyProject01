import random

import pytest
'''
多个参数的参数化
'''
@pytest.mark.parametrize("phone,code",[("18380462343","1234"),("18380465345","4567")])
def test_02(phone,code):
    print(phone)
    print(code)


def num():
    listnum = [10,20,30]
    return listnum

@pytest.mark.parametrize("num",num())
def test_03(num):
    print(num)