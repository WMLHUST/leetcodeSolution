# coding: utf-8

# 两层循环，最里面一层使用夹中法，O(n^3)
# 注意每层循环要越过重复的值

class Solution():
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        i = 0
        while i<len(nums):
            j = i+1
            while j<len(nums):
                left = j+1
                right = len(nums) - 1

                while left < right:
                    cur_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if cur_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[right-1] == nums[right]:
                            right = right - 1

                        while left < right and nums[(left+1)] == nums[left]:
                            left += 1
                        left += 1
                        right -= 1
                    elif cur_sum > target:
                        right -= 1
                    else:
                        left += 1
                while j < len(nums)-1 and nums[j+1] == nums[j]:
                    j += 1
                j += 1
            while i < len(nums)-1 and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return res

nums = [1, 0, -1, 0, -2, 2]
nums = [-3,-2,-1,0,0,1,2,3]
target = 0
print(Solution().fourSum(nums, target))


