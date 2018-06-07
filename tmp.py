# coding: utf-8
def func(tmp, n):
    tmp[:2] = [2, 3]
    tmp = tmp[:2]
    n = 2

l1 = [1, 2, 3]
l2 = [4, 5, 6]
x = 4
if x not in l1 and x not in l2:
    print(True)


d = {1:1, 2:2}
for k, v in d:
    print(k + ',' + v)
