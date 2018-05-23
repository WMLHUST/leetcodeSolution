# coding: utf-8

class Solution:
    def merge2(self, nums1, m, nums2, n):
        if n == 0:
            return

        cur1 = m-1
        cur2 = n-1

        for i in range(m + n):
            j = m+n-1-i

            if cur1 < 0:
                # for x in range(j+1):
                #     nums1[x] = nums2[x]
                nums1[:j+1] = nums2[:cur2+1]
                break
            if cur2 < 0:
                break

            if nums1[cur1] > nums2[cur2]:
                nums1[j] = nums1[cur1]
                cur1 -= 1
            else:
                nums1[j] = nums2[cur2]
                cur2 -= 1

        print(nums1)


# case1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# case2
nums1 = [2,0]
m = 1
nums2 = [1]
n = 1

Solution().merge2(nums1, m, nums2, n)
print(nums1)
