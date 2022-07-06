#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/6 下午11:17

# 如何判断某个对象是不是迭代器
from typing import Iterator


# obj = range(1, 2)
# obj2 = iter(range(1, 3))
#
# for attr in dir(list):
#     print(attr)
#
# for attr in dir(obj):
#     print(attr)
#
# print(isinstance([1, 2], list))
# print(isinstance(obj, Iterator))
# print(isinstance(obj2, Iterator))
# print(isinstance([1, 2], Iterator))


# 自己动手实现一个迭代器
class Next(object):
    def __init__(self, stop, start=0):
        self.start = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        """如果有下一个数，则返回下一个数，如果没有下一个数，则抛出异常：StopIteration"""
        if self.start >= self.stop - 1:
            raise StopIteration
        self.start += 1
        return self.start


if __name__ == '__main__':
    n = Next(5)
    print(n.__next__())
    print(n.__next__())
    print(n.__next__())
    print(n.__next__())
    print(n.__next__())
