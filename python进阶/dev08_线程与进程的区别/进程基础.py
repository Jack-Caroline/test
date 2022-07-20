#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/19 下午11:10
import os
import time
from multiprocessing import Process


def play_music():
    for i in range(5):
        print('play music...')
        time.sleep(1)


def play_lol():
    for i in range(7):
        print('play lol...')
        time.sleep(1)


if __name__ == '__main__':
    # 串行执行
    # play_music()
    # play_lol()

    # 并行执行
    print("主进程ID为：", os.getpid())
    start_time = time.time()
    p1 = Process(target=play_music)
    p2 = Process(target=play_lol)
    p1.daemon = True   # 进程守护，当为 True 时，主进程结束，子进程强制结束；
    p2.daemon = False  # 进程守护，当为 False 时，主进程结束，子进程继续执行；
    p1.start()
    p2.start()
    # p1.join()  # p1未执行完，不能执行下面代码
    # p2.join()  # p2未执行完，不能执行下面代码
    time.sleep(2)
    end_time = time.time()
    print(f"并行运行结束，用时{end_time - start_time}")
