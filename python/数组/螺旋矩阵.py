# coding: utf-8

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # 一层一层递归咯。。注意只有一行或一列的时候，属于边界情况
        def do_traverse(matrix, cur_row, cur_col, deepth):

            row_cnt = len(matrix) - 2 * deepth
            col_cnt = len(matrix[0]) - 2 * deepth
            if row_cnt <= 0 or col_cnt <= 0:
                return []

            res = []
            # 上
            for j in range(col_cnt):
                res.append(matrix[cur_row][cur_col + j])

            # 右
            for i in range(row_cnt - 2):
                res.append(matrix[cur_row + 1 + i][cur_col + col_cnt - 1])

            if row_cnt > 1:
                # 下
                for j in range(col_cnt):
                    tmp = col_cnt - 1 - j
                    res.append(matrix[cur_row + row_cnt - 1][tmp + cur_col])

            if col_cnt > 1:
                # 左
                for i in range(row_cnt - 2):
                    tmp = row_cnt - 3 - i
                    res.append(matrix[tmp + 1 + cur_row][cur_col])

            inner_res = do_traverse(matrix, cur_row + 1, cur_col + 1, deepth + 1)

            return res + inner_res

        if matrix is None or len(matrix) == 0:
            return []
        return do_traverse(matrix, 0, 0, 0)


matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  # [9,10,11,12],
  [13, 14, 15, 16]
]

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]