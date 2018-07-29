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
            # 先存进去的说明在前面
            return [L[tmp], i]


nums = [2, 7, 11, 15]
# nums = [3,2,4]

target = 9
res = twoSum(nums, target)
print(res)