#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/19 下午10:15
"""
Process：进程
multiprocessing.Queue：队列，进程保重的队列方法(管道、序列化、进程安全)
其他管道：MQ（Message Queue）、Redis、rabitMq、kafka
"""
from multiprocessing import Process, Queue


# # 使用列表，work01、work02会重复工作
# def work01(q):
#     while q:
#         print(f'work01 从 q 中获得了{q.pop()}')
#
#
# def work02(q):
#     while q:
#         print(f'work02 从 q 中获得了{q.pop()}')
#
#
# if __name__ == '__main__':
#     q = ['a', 'b', 'c']
#     p1 = Process(target=work01,args=(q,))  # 子进程 q1
#     p2 = Process(target=work02,args=(q,))  # 子进程 q2
#     p1.start()
#     p2.start()
#     print(f"主进程结束")

# 使用队列
def work01(q: Queue):
    while not q.empty():
        print(f'work01 从 q 中获得了{q.get()}')


def work02(q: Queue):
    while not q.empty():
        print(f'work02 从 q 中获得了{q.get()}')


if __name__ == '__main__':
    q = Queue()
    q.put('a')
    q.put('b')
    q.put('c')
    p1 = Process(target=work01, args=(q,))  # 子进程 q1
    p2 = Process(target=work02, args=(q,))  # 子进程 q2
    p1.start()
    p2.start()
    print(f"主进程结束")
