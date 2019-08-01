class Solution:

    # 和课程表1同样的思路，先把无依赖的课找出来，然后先学了。再把这些课学了后，无依赖（实际上是依赖已学的课）的课选出来。直到课程学完。
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        res = []
        seen = {}
        while len(prerequisites)>0:
            mark = [0] * numCourses
            for item in prerequisites:
                mark[item[0]] = 1

            for i in range(numCourses):
                if mark[i] == 0:
                    if i not in seen:
                        res.append(i)
                        seen[i] = 0

            pre_len = len(prerequisites)
            # 小心这里，在删除最后一系列依赖课程，prerequ为空后，由于下次循环不进入，会导致这些课程没被加到res里。
            for item in prerequisites:
                if mark[item[1]] == 0:
                    prerequisites.remove(item)

            aft_len = len(prerequisites)
            if pre_len == aft_len:
                return []

        # prerequisites为空的情况 + 25行提到的最后删除的一系列依赖课程。
        for i in range(numCourses):
            if i not in seen:
                res.append(item[0])
                seen[item[0]] = 1

        return res


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder(numCourses, prerequisites))