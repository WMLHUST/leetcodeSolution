# coding: utf-8

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    col_sets = []
    grid_set = []
    for i in range(0, 9):
        col_sets.append(set())
        grid_set.append(set())

    for i in range(0, 9):
        line = board[i]
        lineSet = set()
        for j in range(0, 9):

            if line[j] == '.':
                continue

            # 判断行
            if line[j] in lineSet:
                return False
            else:
                lineSet.add(line[j])

            # 判断列
            if line[j] in col_sets[j]:
                return False
            else:
                col_sets[j].add(line[j])

            # 判断格子
            g_x = i // 3
            g_y = j // 3
            g_index = int(g_x * 3 + g_y)
            if line[j] in grid_set[g_index]:
                return False
            else:
                grid_set[g_index].add(line[j])
    return True

case = [[".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
print(isValidSudoku(case))