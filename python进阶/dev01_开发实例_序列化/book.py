#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/3 上午10:45
import os
import pickle


class Book(object):
    def __init__(self, num, name, position):
        """初始化"""
        self.num = num
        self.name = name
        self.position = position

    def __str__(self):
        """自定义对象的显示值"""
        return f"{self.num}\t{self.name}\t{self.position}"


class BookManage(object):
    book_list = []

    def __init__(self):
        """加载文件到内存"""
        # 出现问题前处理
        if not os.path.isfile("book.data"):
            pickle.dump(self.book_list, open("book.data", "wb"))
        self.book_list = pickle.load(open("book.data", "rb"))  # 读取文件中的数，加载到内存（反序列化）
        # 避免异常两种方法：一、加判断；二、异常处理；

        # 出现问题后处理
        # try:
        #     self.book_list = pickle.load(open("book.data", "rb"))
        # except FileNotFoundError as e:
        #     print("文件不存在")
        #     pickle.dump(self.book_list, open("book.data", "wb"))
        #     print("文件已创建")

    def __del__(self):
        """把内存中的数据保存到文件"""
        pickle.dump(self.book_list, open("book.data", "wb"))  # 把对象保存到文件（序列化）

    def show_book(self):
        """显示所有图书"""
        for book in self.book_list:
            print(book)

    def add_book(self, book: Book):
        """添加图书"""
        self.book_list.append(book)

    def last_book_id(self):
        """自动生成书籍编号，查询最后一本书的编号，返回其值；如果列表为空返回0"""
        if self.book_list:
            return self.book_list[-1].num
        return 0


if __name__ == '__main__':
    book = Book(1, "吞噬星空", "1号架2层")
    print(book)
