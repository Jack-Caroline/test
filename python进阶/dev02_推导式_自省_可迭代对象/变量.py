#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/5 下午10:32

def test_private_vs_protected_vs_public():
    # public：共有的
    # protected：受保护的   python中 _ 开头
    # private：私有的   python中 __ 开头
    pass


class A(object):
    def __init__(self):
        self.__z = 2  # 私有属性

    def __some_method(self):  # 私有方法
        print(self)

a=A()
print()