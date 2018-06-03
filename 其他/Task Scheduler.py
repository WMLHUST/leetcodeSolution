class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = [0] * 26
        for t in tasks:
            c[ord(t)-ord('A')] += 1

        c.sort()
        i = 25
        while i>=0 and c[i] == c[25]:
            i -= 1

        res = max(len(tasks), (c[25]-1) * (n+1) + (25-i))
        return res

tasks = ["A","A","A","B","B", "B"]
n = 2
print(Solution().leastInterval(tasks, n))