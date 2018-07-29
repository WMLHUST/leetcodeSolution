# coding: utf-8
class Solution(object):
    # 1. 先找到target，存在的话继续找左右边界，不存在返回-1
    # 2. 注意一些边界情况
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def findSmall(nums, left, right):
            mid = (left + right) // 2
            # 注意边界情况，在剩下两个数时会变成死循环，所以在剩下两个数时，不进入循环，左边判断左边是否target（尽可能左）
            while left+1 < right:
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid
                mid = (left + right) // 2

            return left if nums[left]==target else right



        def findLarge(nums, left, right):
            mid = (left + right) // 2
            while left+1 < right:
                if nums[mid] == target:
                    left = mid
                else:
                    right = mid

                mid = (left + right) // 2
            # 右边尽可能右
            return right if nums[right]==target else left

        if len(nums) == 1:
            return [-1, -1] if nums[0]!=target else [0, 0]

        left = 0
        right = len(nums)-1
        mid = (left + right) // 2

        res_start = -1
        res_end = -1
        while left < right:
            if nums[mid]==target:
                res_start = findSmall(nums, left, mid)
                res_end = findLarge(nums, mid, right)
                break
            if nums[mid]>target:
                right = mid
                mid_tmp = (left + right) // 2
                if mid == mid_tmp:
                    mid += 1
                    right -= 1
                else:
                    mid = mid_tmp
            if nums[mid]<target:
                left = mid
                mid_tmp = (left + right) // 2
                if mid == mid_tmp:
                    mid += 1
                    left += 1
                else:
                    mid = mid_tmp

        # 注意判断结束时，索引的值。
        if left == right:
            return [left, left] if nums[left] == target else [-1, -1]
        return [res_start, res_end]


nums = [5,7,7,8,8,10]
# nums = [7, 8]
target = 8
print(Solution().searchRange(nums, target))