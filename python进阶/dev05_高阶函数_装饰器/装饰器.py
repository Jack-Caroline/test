#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/10 下午3:14

"""
装饰器：是一种设计模式
需求：为 字符串 添加修饰，hello ==》<i>hello</i>
"""
from types import FunctionType


def add_itali(func: FunctionType):
    # 倾斜
    def new_func():
        return "<i>" + func() + "</i>"

    return new_func


def add_bold(func: FunctionType):
    # 加粗
    def new_func():
        return "<b>" + func() + "</b>"
    # 返回函数名不要加括号
    return new_func

@add_bold
@add_itali
def text():
    return "Hello"


if __name__ == '__main__':
    print(text())
