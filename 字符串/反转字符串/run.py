# coding: utf-8

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

s = 'hello'
print(reverseString(s))