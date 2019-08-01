class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        cache = {}
        for i in range(0, len(nums)):
            if nums[i] in cache.values():
                nums[i].append(i)
            else:
                cache[nums[i]] = [i]

        res = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                target = 0 - nums[i] - nums[j]
                if target in cache.keys():
                    if i not in cache[target] and j not in cache[target]:
                        tmp = [nums[i], nums[j], target]
                        tmp.sort()
                        if tmp not in res:
                            res.append(tmp)
        print(res)
        return res

    def threeSum2(self, nums):
        res = []
        nums.sort()
        nums_len = len(nums)
        if nums_len<3:
            return []

        i = 0
        while i<nums_len-2:
            target = 0-nums[i]
            left = i+1
            right = nums_len-1
            while left < right:
                if nums[left] + nums[right] == target:
                    tmp_list = [nums[i], nums[left], nums[right]]
                    # res.append(tmp_list)
                    tmp_list.sort()
                    if tmp_list not in res:
                        res.append(tmp_list)
                    left += 1
                    right -= 1
                    continue

                if nums[left] + nums[right] > target:
                    right = right - 1
                else:
                    left += 1

            tmp = nums[i]
            i += 1
            while i<nums_len:
                if nums[i] != tmp:
                    break
                else:
                    i += 1

        return res

nums = [-1,0,1,2,-1,-4, 0, 1, 3]
nums = [-1,0,1,2,-1,-4]
# nums = [0, 0, 1, 1, 1, -1, -1, -1]
nums = []
print(Solution().threeSum2(nums))