# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        i = 0
        j = len(rotateArray) - 1
        mid = (i + j) >> 1
        while i < j-1:
            if rotateArray[mid] >= rotateArray[i]:
                i = mid
            else:
                j = mid
            mid = (i + j) >> 1

        return min(rotateArray[i], rotateArray[j])


print(Solution().minNumberInRotateArray([3, 4, 5, 1]))