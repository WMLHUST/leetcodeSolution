class Solution:

    # 不会，没想通
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0]*len(nums) for _ in nums]

        # 最左边和最右边的1不能戳破
        return self.burst(nums, dp, 1, n)

    # 思想：选定一个范围，遍历，作为最后burst的气球。从burst时间顺序看，是从后到前。
    # 比如刚开始时，确定最后一定是1,x,1，所以遍历所有数，作为x
    # dp里保存的是，以left,right为边界时，捅破气球所能得到的最大值。
    def burst(self, nums, dp, left, right):
        if left > right:
            return 0
        if dp[left][right]>0:
            return dp[left][right]

        res = 0
        # 戳破k
        for k in range(left, right+1):
            left_res = self.burst(nums, dp, left, k-1)
            right_res = self.burst(nums, dp, k+1, right)
            res = max(res, nums[left-1] * nums[k] * nums[right+1] + left_res + right_res)

        dp[left][right] = res
        return res



nums = [3, 1, 5, 8]
print(Solution().maxCoins(nums))
