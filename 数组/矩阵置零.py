# coding: utf-8

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_cnt = len(matrix)
        if row_cnt == 0:
            return
        col_cnt = len(matrix[0])

        row_tmp = -1
        col_tmp = -1
        for i in range(0, row_cnt):
            isFound = False
            for j in range(0, col_cnt):
                if matrix[i][j] == 0:
                    row_tmp = i
                    col_tmp = j
                    isFound = True
                    break
            if isFound:
                break

        if row_tmp<0 and col_tmp<0:
            return

        for i in range(row_tmp, row_cnt):
            for j in range(0, col_cnt):
                if matrix[i][j] == 0:
                    matrix[i][col_tmp] = 0
                    matrix[row_tmp][j] = 0

        for i in range(0, row_cnt):
            if i == row_tmp:
                continue
            if matrix[i][col_tmp] == 0:
                for j in range(0, col_cnt):
                    matrix[i][j] = 0

        for i in range(0, col_cnt):
            if i == col_tmp:
                continue
            if matrix[row_tmp][i] == 0:
                for j in range(0, row_cnt):
                    matrix[j][i] = 0

        for i in range(0, row_cnt):
            matrix[i][col_tmp] = 0
        for j in range(0, col_cnt):
            matrix[row_tmp][j]=0



matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
Solution().setZeroes(matrix)
print(matrix)