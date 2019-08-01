class Solution(object):
    # 关键：避免对前K大的元素排序，借鉴一下快排的思想。时间复杂度，Nlog(K)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]

        cur = nums[0]
        i = 0
        j = len(nums)-1

        while i<j:
            while i<j and nums[j]>cur:
                j -= 1
            if i<j:
                nums[i] = nums[j]
                i += 1

            while i<j and nums[i]<=cur:
                i += 1
            if i<j:
                nums[j] = nums[i]
                j -= 1

        nums[j] = cur
        right_cnt = len(nums) - j - 1
        if right_cnt == k-1:
            return nums[j]

        elif right_cnt >= k:
            return self.findKthLargest(nums[j+1:], k)
        else:
            return self.findKthLargest(nums[:j], k-right_cnt-1)


nums = [3,2,1,5,6,4]
k = 5
print(Solution().findKthLargest(nums, k))

