# coding: utf-8

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums)==0:
            return 1

        min_num = min(nums)
        i, j = 0, 0
        min_num = max(0, min_num)

        # 关键，数组内只保留正数，对正数按照相对位置进行排序，然后再遍历一遍
        while i<len(nums):
            if nums[i]<0:
                nums[i] = 0

            tmp = nums[i] - min_num
            if tmp == i:
                i += 1
                continue

            if tmp >= len(nums) or tmp<0:
                nums[i] = 0
                i += 1
                continue

            if tmp < len(nums) and nums[tmp]!=nums[i]:
                nums[i], nums[tmp] = nums[tmp], nums[i]
                continue
            else:
                nums[i] = 0
                i += 1

        pre_Pos = 0
        for num in nums:
            if num <= 0:
                continue

            # if num>0 and pre_Pos==0:
            #     pre_Pos = num
            #     continue

            if num==pre_Pos+1:
                pre_Pos = num
                continue
            else:
                break

        return pre_Pos+1


nums = [7,8,9,11,12]
# nums = [1, 2, 0]
# nums = [3,4,-1,1]
nums = [-10,-3,-100,-1000,-239,1]
nums = [4,1,3,3]
# nums = [1]
print(Solution().firstMissingPositive(nums))
print(nums)