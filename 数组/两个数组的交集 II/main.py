# coding: utf-8
def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    for i in nums1:
        if i in nums2:
            res.append(i)
            nums2.remove(i)

    return res

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersect(nums1, nums2))
