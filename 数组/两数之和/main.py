# coding: utf-8

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    n = len(nums)
    L = {}
    for i in range(0, n):
        tmp = target - nums[i]
        if tmp not in L:
            L[nums[i]] = i
        else:
            return [i, L[tmp]]

nums = [2, 7, 11, 15]
nums = [3,2,4]

target = 6
res = twoSum(nums, target)
print(res)