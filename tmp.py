# coding: utf-8
def func(tmp, n):
    tmp[:2] = [2, 3]
    tmp = tmp[:2]
    n = 2

tmp = [0, 0, 0]
func(tmp, 0)
print(tmp)