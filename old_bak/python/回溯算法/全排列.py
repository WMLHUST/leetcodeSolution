import copy
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

    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in nums:
            if len(res) == 0:
                res = [[i]]
            else:
                tmp = []
                for j in range(len(res[0])+1):
                    for item in res:
                        item_tmp = copy.deepcopy(item)
                        item_tmp.insert(j, i)
                        tmp.append(item_tmp)
                res = tmp
        return res

n = [1, 2, 3, 4]
res = Solution().permute2(n)
print(len(res))
print(res)