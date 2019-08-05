import random

import pytest

#参数化
@pytest.mark.parametrize("x",[5,4,3,1])

def test_01(x):
    assert x == random.randrange(1,5)



