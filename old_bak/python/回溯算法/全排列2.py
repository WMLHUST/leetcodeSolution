class Solution:
    # 核心还是递归
    # 每次交换第一个数和中间的某个数，作为开头。（这个数没在之前出现过，否则会重复）
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]

        res = []
        seen = set() # 记录做过首数的那些值
        for i in range(len(nums)):
            if i == 0:
                tmp_res = self.permuteUnique(nums[1:])
                seen.add(nums[0])
            elif nums[i] in seen:
                continue
            else:
                seen.add(nums[i])
                nums[i], nums[0] = nums[0], nums[i]
                tmp_res = self.permuteUnique(nums[1:])

            for item_list in tmp_res:
                res.append([nums[0]] + item_list)

        return res
