# coding: utf-8

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False

if __name__=="__main__":
    s = Solution()
    nums = [3,3]
    print(s.containsDuplicate(nums))