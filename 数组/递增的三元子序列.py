# coding: utf-8

# 关键：m1 记录到i为止，最小的数；m2记录的是已有的两个递增数的较大值，所以如果接下来有数大于m2，说明存在三元递增。如果有数比m1大，比m2小，
# 则更新m2，此时m1和m2组成了新的二元递增，而m2保存的依然是两个数里较大的那个。
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m1 = float("inf")
        m2 = float("inf")
        for i in nums:
            if m1 >= i:
                m1 = i
            else:
                if m2 >= i:
                    m2 = i
                else:
                    return True
        return False

nums = [5, 6, 0, 1, 2]
print(Solution().increasingTriplet(nums))