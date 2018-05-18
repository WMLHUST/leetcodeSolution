# coding: utf-8

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    sl = len(s)
    tl = len(t)
    if sl != tl:
        return False

    sc = list(s)
    tc = list(t)
    sc.sort()
    tc.sort()
    for i in range(0, sl):
        if sc[i]!=tc[i]:
            return False

    return True

s = 'hello'
c = 'eholl'
print(isAnagram(s, c))