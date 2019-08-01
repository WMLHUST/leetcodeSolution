import bisect

class Solution:
    # 构造大顶堆，然后pop k次即可
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        h = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(h, matrix[i][j])

        for i in range(k-1):
            heapq.heappop(h)

        return heapq.heappop(h)

    # 临界条件很烦人，注意循环退出唯一条件是small>big
    def kthSmallest2(self, matrix, k):
        smallest = matrix[0][0]
        biggest = matrix[-1][-1]

        while smallest<=biggest:
            mid = (smallest + biggest) // 2
            loc = sum(bisect.bisect_left(row, mid) for row in matrix)
            if loc>=k:
                biggest = mid-1
            else:
                smallest = mid+1

        return biggest


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 9

matrix = [[1,2],[1,3]]
k = 3

matrix = [[1, 2, 3, 3, 4, 4]]
k = 3
print(Solution().kthSmallest2(matrix, k))