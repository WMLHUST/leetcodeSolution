class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findKth(nums1, nums2, k):
            if len(nums1) > len(nums2):
                return findKth(nums2, nums1, k)

            if len(nums1) == 0:
                return nums2[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])

            # 这里才是关键，每次取的是k/2，从而保证比较nums1, nums2的k/2位置的数时，可以删掉k/2的数（这k/2个数一定不包含第k大的数，因为这K/2个数一定小于
            # 特殊情况是，nums1可能小于k/2，这时就取nums1的最后一个数，也是nums1里最大的数，后面递归时，可以删掉k/2或整个nums1
            p1 = int(min(len(nums1), k // 2))
            p2 = k - p1

            if nums1[p1 - 1] == nums2[p2 - 1]:
                return nums1[p1 - 1]

            if nums1[p1 - 1] > nums2[p2 - 1]:
                return findKth(nums1, nums2[p2:], k - p2)
            else:
                return findKth(nums1[p1:], nums2, k - p1)

        n1 = len(nums1)
        n2 = len(nums2)
        if (n1+n2) % 2 != 0:
            return findKth(nums1, nums2, (n1+n2+1)//2)
        else:
            return (findKth(nums1, nums2, (n1+n2)//2) + findKth(nums1, nums2, (n1+n2)//2+1)) / 2

nums1 = [1, 2, 3]
nums2 = [5, 6, 7, 8, 9]
k = 5
print(Solution().findMedianSortedArrays(nums1, nums2))