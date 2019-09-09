# coding: utf-8

class Solution:
    def nextPermutation(self, nums):

        for i in range(len(nums)-1, 0, -1):
            # 找到升序的两个
            if nums[i] > nums[i-1]:
                # swap,找到比i-1大的最小数
                min_index = i
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i-1] and nums[j] < nums[min_index]:
                        min_index = j

                nums[min_index], nums[i-1] = nums[i-1], nums[min_index]

                # 后面的升序
                tmp = nums[i:]
                tmp.sort()
                nums[i:] = tmp
                return

        nums.sort()

nums = [1,3,2]
Solution().nextPermutation(nums)
print(nums)