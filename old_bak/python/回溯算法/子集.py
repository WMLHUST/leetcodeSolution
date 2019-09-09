class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums):
            if len(nums) == 1:
                return [nums]

            res = []

            tmp_res = dfs(nums[1:])

            res.append([nums[0]])
            for item in tmp_res:
                res.append([nums[0]] + item)

            res = res + tmp_res

            return res

        res = dfs(nums)

        return res+[[]]

nums = [1, 2, 3, 4]
print(Solution().subsets(nums))