#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/21 下午11:19

from multiprocessing import Pool
import time


def square(x):
    result = x * x
    return result


if __name__ == '__main__':
    start = time.time()
    pool = Pool(2)
    result = pool.map(square, [1, 2, 3, 4, 5])  # map 会阻塞主程序
    print(result)
    pool.close()
    end = time.time()
    print(f'总共用了{(end - start):.2f}')
