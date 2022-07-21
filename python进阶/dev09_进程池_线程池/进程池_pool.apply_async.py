#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/21 下午11:39
import time
from multiprocessing import Pool

"""
apply：调用函数，传递任意参数
map：把一个可迭代对象 映射 到 函数
"""


def test(x, y):
    return x + y


if __name__ == '__main__':
    pool = Pool(2)
    result = pool.apply(test, (2, 3))  # 阻塞 主程序（主进程）
    print(result)
    # pool.apply_async(test, (2,))  # 不阻塞  主程序

