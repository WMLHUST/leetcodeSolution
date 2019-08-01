class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def getAliveCnt(board, i, j):
            cnt = 0
            # 左上
            if i - 1 >= 0 and j - 1 >= 0:
                cnt += board[i - 1][j - 1] % 2
            # 左
            if j - 1 >= 0:
                cnt += board[i][j - 1] % 2

            # 上
            if i - 1 >= 0:
                cnt += board[i - 1][j] % 2

            # 右上
            if i - 1 >= 0 and j + 1 < len(board[0]):
                cnt += board[i - 1][j + 1] % 2

            # 右
            if j + 1 < len(board[0]):
                cnt += board[i][j + 1] % 2

            # 下
            if i + 1 < len(board):
                cnt += board[i + 1][j] % 2
                if j - 1 >= 0:
                    cnt += board[i + 1][j - 1] % 2
                if j + 1 < len(board[0]):
                    cnt += board[i + 1][j + 1] % 2

            return cnt

        if len(board)==0:
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                alive_cnt = getAliveCnt(board, i, j)
                if board[i][j]==0 and alive_cnt==3:
                    board[i][j] = 2
                    continue
                if board[i][j]==1:
                    if alive_cnt<2 or alive_cnt>3:
                        board[i][j] = 3

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]>=2:
                    board[i][j] = 1 if board[i][j]==2 else 0

board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Solution().gameOfLife(board)
print(board)


