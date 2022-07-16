#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/13 上午12:05

"""
实现一个类，前五次创建对象，以后创建返回5个中随机一个；
"""
import random


class Myclass(object):
    objs = []

    def __new__(cls, *args, **kwargs):
        if len(cls.objs) < 5:
            obj = object.__new__(cls)  # 或者 supper.__new__(cls)
            cls.objs.append(obj)
        else:
            obj = random.choice(cls.objs)
        return obj


class A(object):
    def __init__(self):
        super().__init__()
        print("A......")


class B(object):
    def __init__(self):
        super().__init__()
        print("B......")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C......")


c =C()