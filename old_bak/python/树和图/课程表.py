class Solution:

    # 拓扑排序了解一下：http://www.zhufangxing.com/2015/05/01/leetcode-ICourse%20Schedule/
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        while len(prerequisites)>0:
            mark = [0] * numCourses
            for item in prerequisites:
                mark[item[0]] = 1

            pre_len = len(prerequisites)
            for item in prerequisites:
                if mark[item[1]] == 0:
                    prerequisites.remove(item)
            aft_len = len(prerequisites)
            if pre_len==aft_len:
                return False

        return True
