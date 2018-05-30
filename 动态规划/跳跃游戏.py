class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_dis = 0
        for i in range(0, len(nums)):
            if max_dis >= len(nums)-1:
                return True
            if i<=max_dis and (i + nums[i])>max_dis:
                max_dis = i + nums[i]
            elif i>max_dis:
                return False

nums = [3,2,1,0,4]
print(Solution().canJump(nums))