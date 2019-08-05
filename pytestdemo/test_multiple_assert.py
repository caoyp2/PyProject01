import pytest

#
# @pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
# def test_simple_assume(x, y):
#     pytest.assume(x == y)
#     pytest.assume(True)
#     pytest.assume(False)

def test_multiple_assert():
    pytest.assume(1 == 2)
    pytest.assume(False)
    pytest.assume(True)
