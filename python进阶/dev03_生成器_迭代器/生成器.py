#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/9 下午3:29

# 手动实现平方：传参（1，3） 返回：1，4，9
# 普通
def Squares_list(a, b):
    result = []
    for i in range(a, b + 1):
        result.append(i ** 2)
    print(result)


# 迭代器生成
class Squares(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current


# 生成器实现
def squares(start, stop):
    for i in range(start, stop + 1):
        yield i * i


if __name__ == '__main__':
    # iterator = Squares(1, 3)
    iterator = squares(1, 3)
    for i, value in enumerate(iterator):
        print(i, value)
