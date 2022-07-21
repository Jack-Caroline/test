#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/21 下午11:29

from multiprocessing import Pool

"""
异步
"""

def square(x):
    result = x * x
    return result


if __name__ == '__main__':
    pool = Pool(3)
    result = pool.map_async(square, [1, 2, 3, 4, 5])
    print(result.get())  # get() 获得 map 映射后的结果集
