# coding: utf-8

class Solution(object):

    # 动态规划法
    # 分治法，参考：https://blog.csdn.net/qqxx6661/article/details/78167981，单独计算一次包含中间节点在内的结果就可以了
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