#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/10 下午3:14

"""
filter：过滤 从迭代对象中筛选出满足条件的元素
map：映射
reduce：累加功能
zip：打包
"""
from functools import reduce


def reduce_test():
    def f(x, y):
        result = x + y
        return result

    print(reduce(f, [1, 2, 3, 4, 5, 6, 7]))


def map_test():
    return map(lambda x: (x * 2 + 2), [1, 2, 3])


# print(help(filter))
def filter_test():
    def f(x):
        if x > 2:
            return True
        return False

    return filter(lambda x: x > 2, [1, 2, 3, 4])
    # return filter(f, [1, 2, 3, 4])  # 对[1,2,3,4]一次做判断，大于2的数
    # return filter(None,[1,2,3,4]) 对iterable不做任何操作


if __name__ == '__main__':
    print(reduce_test())
    # item2 = map_test()
    # for i in item2:
    #     print(i)
    # item = filter_test()
    # for i in item:
    #     print(i)
