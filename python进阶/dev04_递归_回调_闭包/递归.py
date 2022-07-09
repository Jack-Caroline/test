#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/9 下午11:36
"""
遍历目录：输出某文件夹下的所有文件的绝对路径（完整的路径）
"""
import os


# 方法一：使用循环来写
def print_all_files(file_path):
    for root, dirs, files in os.walk(file_path):
        for filename in files:
            print(os.path.join(root, filename))


# 使用递归
def print_all_files2(file_path):
    """
    思路：获取file_path下的所有文件及文件夹 os.scandir(file_path)  os.listdir(file_path)
    如果是文件，直接输出
    如果是文件夹，递归调用print_all_files2(文件夹)
    :param file_path:
    :return:
    """
    for item in os.scandir(file_path):
        if item.is_file():
            print(item.path)
        elif item.is_dir():
            print_all_files2(item.path)


if __name__ == '__main__':
    p = "/Users/liangling/Desktop/jack/Python/test/python进阶"
    print_all_files2(p)
