# coding: utf-8

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    curZero = -1

    for i in range(0, n):
        if nums[i]==0:
            curZero = i
            break

    if curZero==-1:
        return

    for i in range(curZero+1, n):
        if nums[i] != 0:
            nums[curZero] = nums[i]
            nums[i] = 0
            curZero += 1

# tc = [0, 1, 0, 3, 12]
tc = [1]
moveZeroes(tc)
print(tc)

