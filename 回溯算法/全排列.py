class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n == 1:
            return [nums]
        for i in range(0, n):
            nums[0], nums[i] = nums[i], nums[0]
            tmp_res = self.permute(nums[1:n])
            for item in tmp_res:
                res.append([nums[0]] + item)

        return res

n = [1, 2]
print(Solution().permute(n))