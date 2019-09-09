class Solution:

    # 厉害哇，两个hash表，把时间复杂度降到了O(n^2)，只想到了利用一个hash表，可以把时间复杂度降到O(n^3)，要多往这方面想想
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sum1 = {}
        for i in A:
            for j in B:
                sum1[i+j] = sum1.get(i+j, 0) + 1

        sum2 = {}
        for i in C:
            for j in D:
                sum2[i+j] = sum2.get(i+j, 0) + 1

        res = 0
        for k, v in sum1.items():
            if -k in sum2:
               res += v * sum2[-k]

        return res

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(Solution().fourSumCount(A, B, C, D))