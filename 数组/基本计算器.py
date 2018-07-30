class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 下一个数字右边界
        def findNextNum(st, i):
            n = len(st)
            num_l = i
            while num_l < n:
                if st[num_l].isdigit():
                    num_l += 1
                else:
                    break
            return num_l

        # 先去除空格
        s = s.replace(' ', '')
        words = []
        i = 0
        while i<len(s):
            if s[i] in ['+', '-', '*', '/']:
                words.append(s[i])
                i += 1
            else:
                next_num_l = findNextNum(s, i)
                if next_num_l <= len(s):
                    words.append(int(s[i:next_num_l]))
                i = next_num_l


        # 遍历一遍，先计算乘除，切记切记
        s = words
        hasCC = True
        i = 0
        while hasCC:
            hasCC = False
            while i<len(s):
                if s[i] == '*':
                    tmp = int(s[i-1]) * int(s[i+1])
                elif s[i] == '/':
                    tmp = int(s[i - 1]) // int(s[i + 1])
                else:
                    i+=1
                    continue

                hasCC = True
                del s[i+1]
                del s[i]
                del s[i - 1]
                s.insert(i-1, tmp)
                break

        n = len(s)
        i = 1
        res = s[0]
        while i<n:
            if s[i] == '+':
                res = res + int(s[i+1])
            elif s[i] == '-':
                res = res - int(s[i+1])
            i = i + 2

        return res

s = " 3+5 / 2 "
# s = "42"
# s = "3+2*2"
print(Solution().calculate(s))