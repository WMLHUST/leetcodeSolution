class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums_sum = sum(nums)
        return n*(n+1)/2-nums_sum

# 除下求和还有一个方法也很机智
# 利用两个相同数的异或==0
# 所以可以先算一个0 ~ len(nums)+1的异或值，再和nums里的数依次异或抵消。