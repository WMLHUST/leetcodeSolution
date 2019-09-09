class Solution(object):
    # 两端无穷小，因此只需找到一个n < n+1 或 n>n-1，目标必在这两个范围里存在。
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return 0

        if nums[0]>nums[1]: return 0
        if nums[n-1]>nums[n-2]: return n-1

        left = 0
        right = n-1
        mid = n // 2
        while True:
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid

            # 不是峰值，mid-1和mid+1必有一个>mid
            if nums[mid] < nums[mid-1]:
                right = mid
                mid = (left + mid) // 2
                continue

            if nums[mid] < nums[mid+1]:
                left = mid
                mid = (mid + right) // 2

nums = [1,2,1,3,5,6,4]
print(Solution().findPeakElement(nums))