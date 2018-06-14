class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left_product = [0] * len(nums)
        left_product[0] = nums[0]
        for i in range(1, len(nums)):
            left_product[i] = nums[i] * left_product[i-1]

        right_cur = 1
        for i in range(len(nums)-1, 0, -1):
            left_product[i] = left_product[i-1] * right_cur
            right_cur *= nums[i]

        left_product[0] = right_cur
        return left_product

nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))