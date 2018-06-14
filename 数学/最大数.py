class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key

        def cmp(x, y):
            # print(x, y)
            if str(x)+str(y) > str(y)+str(x):
                # print("return True")
                return 1
            elif str(x)+str(y) < str(y)+str(x):
                return -1
            else:
                return 0

        keys = cmp_to_key(cmp)
        nums.sort(key=keys, reverse=True)
        res = ''.join(map(str, nums)).lstrip('0')
        return res or '0'

nums = [2, 10]
print(Solution().largestNumber(nums))