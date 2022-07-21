#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/21 下午9:49

import time
import threading


def music(user):
    print(f"{user}正在听音乐....")
    print(f"{threading.current_thread().name}正在运行......")
    time.sleep(5)
    print(f"{threading.current_thread().name}运行运行结束")


def lol(user):
    time.sleep(8)


if __name__ == '__main__':
    t1 = threading.Thread(target=music, args=('小贱',), name='线程1')
    t2 = threading.Thread(target=lol, args=('小贱',), name='线程2')
    t1.start()
    t2.start()
    t1.join()  # 阻塞主程序，但不会阻塞线程2
    t2.join()
    print("主程序结束！")
