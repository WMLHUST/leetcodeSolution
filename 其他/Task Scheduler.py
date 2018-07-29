class Solution(object):
    # 参考 https://blog.csdn.net/Koala_Tree/article/details/78498586
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

        # 选取任务数最多的那些任务类别，其实是计数。。
        max_cnt = c[25]
        max_cnt_task_cnt = 0
        for cnt in c[::-1]:
            if cnt == max_cnt:
                max_cnt_task_cnt += 1
            else:
                break

        # (c[25]-1)*(n+1)，是数量最多的那单个任务所需的时间，25-i是数量最多的不同任务个数，因为前面少算一个排列，如ABxxAB里最后的AB
        res = max(len(tasks), (c[25]-1) * (n+1) + max_cnt_task_cnt)
        return res

tasks = ["A","A","A","B","B", "B"]
n = 2
print(Solution().leastInterval(tasks, n))