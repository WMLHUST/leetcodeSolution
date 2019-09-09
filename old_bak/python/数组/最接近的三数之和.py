# coding: utf-8

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        min_gap = float('inf')
        res = 0
        # 固定一个值
        # 然后剩下的数，夹中法
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(target - cur_sum) < min_gap:
                    min_gap = abs(target-cur_sum)
                    res = cur_sum
                    if min_gap == 0:
                        return res

                # 移动
                if cur_sum > target:
                    right -= 1
                else:
                    left += 1
        return res

nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(nums, target))

