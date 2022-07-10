#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/10 下午3:02
"""
nums = [1,22,33,4,7,-1]  ==> [22,33,7]
把大于5的数过滤出来，放到一个新列表中
"""


def filter_nums1(nums, mark=5):
    nums_new = []
    for i in list:
        if i > mark:
            nums_new.append(i)
    return nums_new


def filter_nums2(nums, mark=5):
    return list(filter(lambda x: x > 5, nums))


nums = [1, 22, 33, 4, 7, -1]
print(filter_nums1(nums))
