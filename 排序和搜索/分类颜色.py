class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums)-1
        while i<k:
            if nums[i] == 0:
                i += 1
                continue

            if nums[i] == 1:
                pass

    def sortColors2(self, nums):
        i = -1
        j = -1
        k = -1

        for m in range(len(nums)):
            if nums[m]==0:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1
                i += 1
                nums[i] = 0

            elif nums[m] == 1:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1

            else:
                k += 1
                nums[k] = 2

nums = [2, 0, 2, 2, 1, 1, 1, 0]
Solution().sortColors2(nums)
print(nums)

