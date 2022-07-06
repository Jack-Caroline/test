#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/6 下午11:13

def my_range(stop):
    """模拟python2中range，当数量比较多的时候会比较慢"""
    value = 1
    result = []
    while value < stop:
        result.append(value)
        value += 1
    return result


if __name__ == '__main__':
    print(my_range(10))
