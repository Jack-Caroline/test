#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/22 上午12:22
import threading

n = 200000
lock = threading.Lock()  # 创建锁的对象


def work():
    global n
    for i in range(1000000):
        # 上锁
        lock.acquire()
        n -= 1
        # 释放锁
        lock.release()


if __name__ == '__main__':
    # 两个程序共同操作
    t1 = threading.Thread(target=work)
    t2 = threading.Thread(target=work)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
