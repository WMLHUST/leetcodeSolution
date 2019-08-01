# coding: utf-8

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    if n==1:
        return
    begin_x = 0
    begin_y = 0
    next_x = begin_y
    next_y = n - 1 - begin_x
    last = matrix[begin_x][begin_y]

    # 这个应该用递归更简单，不用这么复杂的循环
    for i in range(0, n*n):
        if next_x==begin_x and next_y == begin_y:
            matrix[next_x][next_y] = last
            begin_y += 1
            # 外圈搞完，搞下一层内圈
            if begin_y >= n-1-begin_x:
                begin_x += 1
                begin_y = begin_x

            last = matrix[begin_x][begin_y]
            next_x = begin_y
            next_y = n - 1 - begin_x

            continue

        tmp = matrix[next_x][next_y]
        matrix[next_x][next_y] = last
        last = tmp

        cur_x = next_x
        cur_y = next_y
        next_x = cur_y
        next_y = n-1 - cur_x

    return matrix

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

matrix2 = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

matrix3 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(rotate(matrix))
