#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2021/12/23 14:52


def add_itali(func):
    """接收一个函数，返回一个经过装饰的新函数"""
    def new_fun():
        return "<i>" + func() + "</i>"
    # 返回函数名，不要加括号
    return new_fun


def add_hold(func):
    def new_func():
        return "<b>" + func() + "</b>"
    return new_func


@add_itali
@add_hold
def text():
    return "hello"


if __name__ == '__main__':
    print(text())
