# coding: utf-8

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        while i<len(s):

            if s[i] == 'I':
                if i+1 >= len(s):
                    res += 1
                    break
                if s[i+1] == 'V':
                    res += 4
                    i = i+2
                elif s[i+1] == 'X':
                    res += 9
                    i = i+2
                else:
                    res += 1
                    i = i + 1
                # for j in range(i+1, len(s)):
                #     if s[j] != 'I':
                #         break
                # res += (j-i)
                # i = j+1

            elif s[i] == 'V':
                res += 5
                i += 1
            elif s[i] == 'X':
                if i+1 >= len(s):
                    res += 10
                    break
                if s[i+1] == 'L':
                    res += 40
                    i = i+2
                elif s[i+1] == 'C':
                    res += 90
                    i = i+2
                else:
                    res += 10
                    i = i + 1

            elif s[i] == 'L':
                res += 50
                i+=1
            elif s[i]=='C':
                if i+1 >= len(s):
                    res += 100
                    break
                if s[i+1] == 'D':
                    res += 400
                    i = i+2
                elif s[i+1] == 'M':
                    res += 900
                    i = i+2
                else:
                    res += 100
                    i = i + 1
            elif s[i] == 'D':
                res += 500
                i+=1
            elif s[i] == 'M':
                res += 1000
                i+=1
            else:
                print("error")

        return res

s = "LVIII"
print(Solution().romanToInt(s))