class Solution:

    # 对每个值做dfs，为了避免重复对单个节点重复dfs，可以提前把每个节点的dfs结果存起来。
    # 也不用担心会出现重复访问某个节点造成循环，因为条件是 递增。只有满足递增条件的才会进行下一步的move
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        def move(matrix, i, j):
            if dis_dict[i][j]!=0:
                return dis_dict[i][j]

            cur = matrix[i][j] #临时记录原始值
            row_cnt = len(matrix)
            col_cnt = len(matrix[0])

            tmp_max = 0
            # 上
            if i-1>=0 and matrix[i-1][j]>cur:
                next_move_cnt = move(matrix, i-1, j)
                tmp_max = max(next_move_cnt, tmp_max)

            # 下
            if i+1<=row_cnt-1 and matrix[i+1][j]>cur:
                next_move_cnt = move(matrix, i + 1, j)
                tmp_max = max(next_move_cnt, tmp_max)

            # left
            if j-1>=0 and matrix[i][j-1]>cur:
                next_move_cnt = move(matrix, i, j-1)
                tmp_max = max(next_move_cnt, tmp_max)

            # right
            if j+1<=col_cnt-1 and matrix[i][j+1]>cur:
                next_move_cnt = move(matrix, i, j + 1)
                tmp_max = max(next_move_cnt, tmp_max)

            return tmp_max+1

        if len(matrix)==0:
            return 0

        row_cnt = len(matrix)
        col_cnt = len(matrix[0])

        dis_dict = [[0 for j in range(col_cnt)] for i in range(row_cnt)]

        res_max = 0
        for i in range(row_cnt):
            for j in range(col_cnt):
                res_tmp = move(matrix, i, j)
                res_max = max(res_max, res_tmp)
                dis_dict[i][j] = res_tmp
        return res_max

    def longestIncreasingPath2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.record = {}

        def dfs(matrix, i, j, deepth):
            if (i, j) in self.record:
                return self.record[(i, j)]

            res = deepth
            if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
                up_res = dfs(matrix, i - 1, j, deepth)
                res = max(res, up_res)

            if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
                left_res = dfs(matrix, i, j - 1, deepth)
                res = max(res, left_res)

            if i + 1 < len(matrix) and matrix[i][j] < matrix[i + 1][j]:
                down_res = dfs(matrix, i + 1, j, deepth)
                res = max(res, down_res)

            if j + 1 < len(matrix[0]) and matrix[i][j] < matrix[i][j + 1]:
                right_res = dfs(matrix, i, j + 1, deepth)
                res = max(res, right_res)

            return res+1

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tmp = dfs(matrix, i, j, 0)
                res = max(res, tmp)
                self.record[(i, j)] = tmp

        return res

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

nums = [[9,9,4],[6,6,8],[2,1,1]]

nums = [[7,8,9],
        [9,7,6],
        [7,2,3]]

nums = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
print(Solution().longestIncreasingPath(nums))