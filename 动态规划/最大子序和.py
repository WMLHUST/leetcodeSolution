# coding: utf-8

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        res = nums[0]
        F_Max = nums[0]
        for i in range(1, len(nums)):
            F_Max = max(F_Max + nums[i], nums[i])
            res = max(res, F_Max)

        return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))