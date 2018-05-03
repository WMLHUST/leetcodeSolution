# coding: utf-8

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 按位异或，最后留下单独的那个数
    res = 0
    for i in nums:
        res = res ^ i

    return res

nums = [4,1,2,1,2]
print(singleNumber(nums))