#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/3 下午6:58

def test_derivation():
    """
    推导式的格式
    [ 处理迭代中的每一个元素 for 语句 判断条件]
    :return:
    """
    result = []
    for i in range(1, 101):
        if i % 2 == 0:
            result.append(i)
    print(result)

    print([i for i in range(1, 101) if i % 2 == 0])  # 列表推导式  列表解析

    # 用于字典的解析
    # 字典推导式 字典解析 格式如下：
    # {键: 值 for 语句}
    cookie = """  """
    new_cookie = {}
    for item in cookie.split(";"):  # 先用 ；分割 cookies
        s = item.split("=")  # 用 = 分割
        new_cookie[s[0]] = s[1]  # =左边作为键，=右边作为值，添加到 new_cookie 字典中；
    print(new_cookie)  # 输出 new_cookie

    print({item.split("=")[0]: item.split("=")[1] for item in cookie.split(";")})  # 字典推导式


if __name__ == '__main__':
    test_derivation()
