class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = 0 if m==0 else len(matrix[0])
        if m==0 and n==0:
            return False

        i = 0
        j = n-1
        while i<m and j>=0:
            if matrix[i][j] == target:
                return True

            elif matrix[i][j]<target:
                i += 1

            elif matrix[i][j]>target:
                j -= 1

        return False

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 20
print(Solution().searchMatrix(matrix, target))
