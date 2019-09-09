# coding: utf-8

class Solution:
    def searchInsert(self, nums, target):
        i = 0
        j = len(nums)-1
        mid = (i+j)>>1
        while i<j-1:
            if nums[mid]>=target:
                j = mid
            elif nums[mid]<target:
                i = mid

            mid = (i+j)>>1

        if nums[i] >= target:
            return i
        elif nums[j] < target:
            return j+1
        else:
            return j

nums = [1,3,5,6]
target = 7
print(Solution().searchInsert(nums, target))