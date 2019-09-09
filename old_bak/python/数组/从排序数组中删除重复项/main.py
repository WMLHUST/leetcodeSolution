# coding: utf-8

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = len(nums)
        if cnt<2:
            return cnt
        i = 0
        j = 1
        while j<cnt:
            if nums[i]==nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
                j += 1

        return i+1

if __name__=='__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    print(solution.removeDuplicates(nums))
