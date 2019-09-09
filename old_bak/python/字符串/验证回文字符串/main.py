# coding: utf-8

def isPalindrome(s):
    n = len(s)
    if n==0:
        return True
    else:
        i=0;j=n-1
        while True:
            while True:
                if s[i].isalpha() or s[i].isdigit():
                    break
                else:
                    i+=1
                    if i >= j:
                        return True

            while True:
                if s[j].isalpha() or s[j].isdigit():
                    break
                else:
                    j-=1
                    if i >= j:
                        return True

            if i>=j:
                return True
            elif s[i].lower()!=s[j].lower():
                return False
            else:
                i+=1;j-=1

def isPalindrome2(s):
    sc = list(filter(str.isalnum, s.lower()))
    return sc == sc[::-1]


print(isPalindrome2('A man, a plan, a canal: Panama'))

