# coding: utf-8

def firstUniqChar(s):
    n = len(s)
    # tmp保存的是 字符:索引
    tmp = {}
    for i in range(0, n):
        if s[i] not in tmp:
            tmp[s[i]] = i
        else:
            tmp[s[i]] = n+1

    min = n+1
    for i in tmp.values():
        if i<min:
            min = i
    if min==n+1:
        return -1
    else:
        return min

print(firstUniqChar("heeh"))
print(firstUniqChar("aadadaad"))
print(firstUniqChar("loveleetcode"))
