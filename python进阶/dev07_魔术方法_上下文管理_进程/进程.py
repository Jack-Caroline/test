#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/16 下午6:58
"""
需求：使用多线程实现并发下载图片
"""
from multiprocessing import Process, Queue

import requests


# def init_task():
#     tasks = Queue()
#     tasks.put("http://aaa.jpg")
#     tasks.put("http://bbb.jpg")


def download(q: Queue):
    while True:
        url = q.get()
        r = requests.get(url)
        img_name = url.split('/')[-1]
        with open(img_name,"wb") as f:
            f.write(r.content)
        if q.empty():
            break


if __name__ == '__main__':
    tasks = Queue()
    tasks.put("https://qq.yh31.com/tp/kx/202206272059134612.jpg")
    tasks.put("https://qq.yh31.com/tp/xg/202205032135427556.jpg")

    p1 = Process(target=download, args=(tasks,))
    p2 = Process(target=download, args=(tasks,))
    p1.start()
    p2.start()
