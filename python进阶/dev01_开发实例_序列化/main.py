#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/3 上午10:45
from python进阶.dev01_开发实例_序列化.book import *


def welcome():
    print("****************欢迎进入图书管理系统********************")
    print("1、显示所有图书\n2、添加图书\n3、删除图书\n4、查找图书\n5、退出")
    print("*****************************************************")


def get_choose_number():
    """获得用户输入的菜单编号"""
    choose_number = input("请输入菜单编号")  # 是一个字符串，需要转化
    # 如果不是数字、或者 不是1、2、3、4 返回 -1
    if not choose_number.isdigit() and choose_number not in [1, 2, 3, 4]:
        return -1
    return int(choose_number)


def main():
    bm = BookManage()
    while True:
        welcome()
        number = get_choose_number()
        if number == -1:
            print("输入有误，请重新输入")
            continue
        if number == 1:
            bm.show_book()
        elif number == 2:
            num = bm.last_book_id() + 1
            book_name = input("请输入书名")
            book_position = input("请输入位置")
            book = Book(num, book_name, book_position)
            bm.add_book(book)
        elif number == 3:
            pass
        elif number == 4:
            pass
        else:
            break


if __name__ == '__main__':
    main()
