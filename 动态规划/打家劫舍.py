# coding: utf-8

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        F_N_2 = nums[0]
        F_N_1 = max(nums[0], nums[1])
        res = max(F_N_1, F_N_2)

        for i in range(2, len(nums)):
            F_cur = max(F_N_2 + nums[i], F_N_1)
            F_N_2, F_N_1 = F_N_1, F_cur
            res = max(res, F_cur)

        return res