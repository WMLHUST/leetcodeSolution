# coding: utf-8

@staticmethod
def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    res = ""
    n = len(s)
    for i in range(0, n):
        res += s[n-1-i]
    return res

def reverse(x):
    if x==0:
        return 0

    iMax = pow(2, 31)-1
    iMin = -pow(2, 31)
    if x>0:
        s = str(x)
        res = int(reverseString(s))
        if res>iMax:
            return 0
        else:
            return res
    else:
        s = str(x)[1:]
        res = -int(reverseString(s))
        if res < iMin:
            return 0
        else:
            return res

# 不得不说，如果用C/C++，要麻烦不少。。
print(reverse(123))