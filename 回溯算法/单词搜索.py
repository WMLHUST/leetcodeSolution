class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        marks = [[0]*n for _ in range(m)]

        def dfs(i, j, w_index, marks):
            if w_index == len(word):
                return True

            if i - 1 >= 0:
                if marks[i - 1][j] == 0 and board[i - 1][j] == word[w_index]:
                    marks[i - 1][j] = 1
                    res = dfs(i-1, j, w_index+1, marks)
                    if res == True:
                        return True
                    else:
                        marks[i-1][j] = 0
            if i + 1 <= m - 1:
                if marks[i + 1][j] == 0 and board[i + 1][j] == word[w_index]:
                    marks[i + 1][j] = 1
                    res = dfs(i + 1, j, w_index+1, marks)
                    if res == True:
                        return True
                    else:
                        marks[i+1][j] = 0
            if j - 1 >= 0:
                if marks[i][j - 1] == 0 and board[i][j - 1] == word[w_index]:
                    marks[i][j - 1] = 1
                    res = dfs(i, j-1, w_index+1, marks)
                    if res == True:
                        return True
                    else:
                        marks[i][j-1] = 0
            if j + 1 <= n-1:
                if marks[i][j + 1] == 0 and board[i][j + 1] == word[w_index]:
                    marks[i][j + 1] = 1
                    res = dfs(i, j+1, w_index+1, marks)
                    if res == True:
                        return True
                    else:
                        marks[i][j+1] = 0
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    marks[i][j] = 1
                    res = dfs(i, j, 1, marks)
                    if res:
                        return True
                    else:
                        marks[i][j] = 0

        return False

board = \
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

board = [['a', 'a']]

board = [["C","A","A"],
         ["A","A","A"],
         ["B","C","D"]]
s = "AAB"
print(Solution().exist(board, s))



