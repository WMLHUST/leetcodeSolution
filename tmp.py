def binnarySearch(nums_ordered, cur):
    if len(nums_ordered) == 0:
        return 0

    left = 0
    right = len(nums_ordered) - 1
    if cur <= nums_ordered[left]:
        return 0
    if cur > nums_ordered[right]:
        return right + 1

    mid = (left + right) // 2
    while left < right - 1:
        if cur <= nums_ordered[mid]:
            right = mid
        elif cur > nums_ordered[mid]:
            left = mid

        mid = (left + right) // 2

    return right

nums = [1, 2, 3, 4]
cur = 4
print(binnarySearch(nums, cur))