#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/9 下午11:36

# 比较2个数的大小，并用不同风格输出
def get_min(a, b, func):
    # func 是回调函数的引用
    result = a if a < b else b
    func(a, b, result)


# 回调函数一
def call_back_print_en(a, b, _min):
    print(f"compare {a} and {b},min={_min}")


# 回调函数二
def call_back_print_zh(a, b, _min):
    print(f"{a} 和 {b} 比较，{_min}最小")


if __name__ == '__main__':
    get_min(1, 2, call_back_print_en)
    get_min(1, 2, call_back_print_zh)
