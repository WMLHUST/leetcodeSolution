# coding: utf-8

# 牛顿迭代法，用切线去逼近高次方程的解
def mySqrt(x):
    n = 1
    while True:
        m = n/2 + x/2/n
        if abs(m-n)<0.001:
            break
        n = m
    return m
print(mySqrt(2))