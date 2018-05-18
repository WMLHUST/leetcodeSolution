# coding: utf-8

def myAtoi(s):
    INT_MIN = -pow(2, 31)
    INT_MAX = pow(2, 31)-1
    s = s.strip()
    n = len(s)
    if n==0:
        return 0
    elif not (s[0].isdigit() or s[0]=='-' or s[0]=='+'):
        return 0
    elif n==1 and s[0]=='-':
        return 0

    isNeg = False
    if s[0]=='-':
        isNeg = True
        s = s[1:]
    elif s[0]=='+':
        s = s[1:]

    n = len(s)
    s2 = ''
    for i in range(0, n):
        # if s[i] == ' ':
        #     continue
        if s[i].isdigit():
            s2 += s[i]
        else:
            break
    if len(s2)==0:
        return 0

    res = int(s2)
    if isNeg:
        res = -res

    if res<INT_MIN:
        return INT_MIN
    elif res>INT_MAX:
        return INT_MAX

    return res

print(myAtoi('+1'))