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
            # matrix[i][j] = float('-inf')
            row_cnt = len(matrix)
            col_cnt = len(matrix[0])

            tmp_max = 0
            # 上
            if i-1>=0 and matrix[i-1][j]>cur:
                # tmp = matrix[i-1][j]
                # matrix[i-1][j] = -float('inf')
                next_move_cnt = move(matrix, i-1, j)
                tmp_max = max(next_move_cnt, tmp_max)
                # matrix[i-1][j] = tmp

            # 下
            if i+1<=row_cnt-1 and matrix[i+1][j]>cur:
                # tmp = matrix[i + 1][j]
                # matrix[i + 1][j] = -float('inf')
                next_move_cnt = move(matrix, i + 1, j)
                tmp_max = max(next_move_cnt, tmp_max)
                # matrix[i + 1][j] = tmp

            # left
            if j-1>=0 and matrix[i][j-1]>cur:
                # tmp = matrix[i][j-1]
                # matrix[i][j-1] = -float('inf')
                next_move_cnt = move(matrix, i, j-1)
                tmp_max = max(next_move_cnt, tmp_max)
                # matrix[i][j-1] = tmp

            # right
            if j+1<=col_cnt-1 and matrix[i][j+1]>cur:
                # tmp = matrix[i][j + 1]
                # matrix[i][j + 1] = -float('inf')
                next_move_cnt = move(matrix, i, j + 1)
                tmp_max = max(next_move_cnt, tmp_max)
                # matrix[i][j + 1] = tmp

            # matrix[i][j] = cur
            dis_dict[i][j] = tmp_max + 1
            return tmp_max+1

        if len(matrix)==0:
            return 0

        row_cnt = len(matrix)
        col_cnt = len(matrix[0])

        dis_dict = [[0 for j in range(col_cnt)] for i in range(row_cnt)]

        res_max = 0
        for i in range(row_cnt):
            for j in range(col_cnt):
                # tmp = matrix[i][j]
                # matrix[i][j] = float('-inf')
                res_tmp = move(matrix, i, j)
                # matrix[i][j] = tmp
                res_max = max(res_max, res_tmp)

        return res_max

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
print(Solution().longestIncreasingPath(nums))