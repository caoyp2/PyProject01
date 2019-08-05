'''
带参数的fixture
'''

import pytest


@pytest.fixture(params=[1,5,7])
def test_data(request):
    return request.param


def test_01(test_data):
    print('test_data: %s' % test_data)
    assert test_data != 5

if __name__ == "__main__":
    pytest.main("-v","-s","test_fixture_param.py")