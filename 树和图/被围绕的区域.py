class Solution:

    # 从边界入手。。把和边界上的0相连的0都标记出来，这些是围绕不住的。
    # 剩下的0，都是被围绕的区域
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def setAround(board, i, j):
            row_cnt = len(board)
            col_cnt = len(board[0])

            # 上
            if i-1>=0:
                if board[i-1][j] == 'O':
                    board[i-1][j] = '#'
                    setAround(board, i-1, j)
            # 下
            if i+1<=row_cnt-1:
                if board[i+1][j] == 'O':
                    board[i+1][j] = '#'
                    setAround(board, i+1, j)
            # 左
            if j-1>=0:
                if board[i][j-1] == 'O':
                    board[i][j-1] = '#'
                    setAround(board, i, j-1)
            # 右
            if j+1<=col_cnt-1:
                if board[i][j+1] == 'O':
                    board[i][j+1] = '#'
                    setAround(board, i, j+1)

        if len(board)==0:
            return
        row_cnt = len(board)
        col_cnt = len(board[0])

        for i in range(row_cnt):
            if board[i][0] == 'O':
                board[i][0] = '#'
                setAround(board, i, 0)
            if board[i][col_cnt-1] == 'O':
                board[i][col_cnt-1] = '#'
                setAround(board, i, col_cnt-1)

        for j in range(col_cnt):
            if board[0][j] == 'O':
                board[0][j] = '#'
                setAround(board, 0, j)
            if board[row_cnt-1][j] == 'O':
                board[row_cnt-1][j] = '#'
                setAround(board, row_cnt-1, j)

        for i in range(row_cnt):
            for j in range(col_cnt):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["X","O","X"],
         ["O","X","O"],
         ["X","O","X"]]
Solution().solve(board)
print(board)

