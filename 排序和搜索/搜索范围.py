# coding: utf-8
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findSmall(nums, left, right):
            mid = (left + right) // 2
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
        if left == right:
            return [left, left] if nums[left] == target else [-1, -1]
        return [res_start, res_end]


nums = [5,7,7,8,8,10]
# nums = [7, 8]
target = 8
print(Solution().searchRange(nums, target))