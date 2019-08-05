'''
测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有 init 方法
测试函数以test_开头
断言使用基本的assert即可
'''
#! /usr/bin/env python
#coding=utf-8

import random
import pytest


def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return random.choice([nums,None,10])

#失败重跑应用
@pytest.mark.flaky(reruns=5)
def test_sort():
    assert bubble_sort([9,5,8,6]) == [5,6,8,9]

