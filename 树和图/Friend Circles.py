class Solution:

    # 这种划分区域的题，用dfs，直接在图上做标记，同一套路
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(M, cur):
            M[cur][cur] = 0
            for j in range(0, len(M)):
                if M[cur][j] == 1:
                    M[cur][j] = 0
                    dfs(M, j)

        n = len(M)
        res = 0
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    res += 1
                    M[i][j] = 0
                    dfs(M, j)

        return res


M = [[1,1,0],
 [1,1,0],
 [0,0,1]]

# M = [[1,1,0],
#      [1,1,1],
#      [0,1,1]]

# M = [[1,0,0,1],
#      [0,1,1,0],
#      [0,1,1,1],
#      [1,0,1,1]]
print(Solution().findCircleNum(M))
