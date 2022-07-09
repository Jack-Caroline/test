#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/9 下午11:36

# 记录任何函数执行的日志
import logging


def logger(func):
    def log_func(*args):
        logging.basicConfig(filename="dome.log", level=logging.INFO)
        logging.info(f"{func.__name__} is running, arguments is {args}")
        func(*args)

    # 返回 log_func 不加括号，这就是闭包
    return log_func


def f1(a, b):
    print(a)


def f2(x, y):
    print(x)

f1_logger = logger(f1)
f2_logger = logger(f2)
f1_logger(1,2)
f2_logger(10,20)


