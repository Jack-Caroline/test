#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/3 下午5:01
import pickle

# li = [1, 2, 3, 4, 5]
#
# pickle.dump(li,open("demo.data","wb"))

l = pickle.load(open("demo.data","rb"))
print(l)