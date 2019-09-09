class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return nums[0]
        max_dp = [0] * n
        min_dp = [0] * n
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        for i in range(1, len(nums)):
            max_dp[i] = max(nums[i], nums[i]*max_dp[i-1], nums[i]*min_dp[i-1])
            min_dp[i] = min(nums[i], nums[i]*max_dp[i-1], nums[i]*min_dp[i-1])

        return max(max_dp)

nums = [2,3,-2,4]
print(Solution().maxProduct(nums))