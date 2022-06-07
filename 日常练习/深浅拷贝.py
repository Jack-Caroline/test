#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/7 9:31
import copy

# 浅拷贝
# a = "where"
# b = 5
c = [1, 2, 3, 4, "q", "w", "e", "r"]
d = {1: "a", 2: "b", 3: "c", 4: "d", 5: [1, 2, 3, 4, "O"]}
# e = (1, 2, 3, 4)

# a1 = a.copy()
# b1 = b.copy()
c1 = c.copy()
d1 = d.copy()
# e1 = e.copy()

# print("a1为{}".format(a1))
# print("b1为 %s", "b1")
print(f'{"c1为"}{c1}')
print("d1为{}".format(d1))
print("---------------------------------------")
# print("e1为" + e1)
c.append(7)
d[6] = 9
print(f'{"c为"}{c}')
print("d为{}".format(d))
print(f'{"c1为"}{c1}')
print("d1为{}".format(d1))
print("---------------------------------------")

c[0] = 0
d[5].append("5")
print(f'{"c为"}{c}')
print("d为{}".format(d))
print(f'{"c1为"}{c1}')
print("d1为{}".format(d1))
print("---------------------------------------")

# 深拷贝
a = [1, 2, 3, 4, 5, [6, 7, 8, 9]]
b = {1: 123, 2: 456, 3: [7, 8, 9]}

a1 = copy.deepcopy(a)
b1 = copy.deepcopy(b)

print(a)
print(b)
print(a1)
print(b1)
print("---------------------------------------")

a.append(10)
b[4] = "abc"
print(a)
print(a1)
print(b)
print(b1)
print("---------------------------------------")

a[5].append(11)
b[3].append(10)
print(a)
print(a1)
print(b)
print(b1)
print("---------------------------------------")