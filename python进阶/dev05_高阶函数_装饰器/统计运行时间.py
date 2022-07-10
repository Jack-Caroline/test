#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/10 下午7:12
import time


def call_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} 运行了 {end - start} 时间')

    return wrapper


@call_time
def f(list):
    nums = 0
    for i in list:
        nums += i
    return nums


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num = f(list)
    print(num)
