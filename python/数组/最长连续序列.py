class Solution:

    # 不能使用相对位置存储的方法。。因为结果不一定都是从1开始的。
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums)==0:
            return 0

        vals = {}
        for num in nums:
            vals[num] = 1

        for num in nums:
            if vals[num] > 1:
                continue

            # 找左边
            res1 = 1
            cur = num
            while (cur-1) in vals:
                vals[cur-1] = res1 + 1
                cur = cur - 1
                res1 = res1 + 1

            # 找右边
            res2 = 1
            cur = num
            while (cur+1) in vals:
                vals[num+1] = res2+1
                cur = cur + 1
                res2 = res2 +1

            # 注意要把左右两个方向的结果相加
            vals[num] = res1 + res2 - 1

        return max(vals.values())

nums = [100, 4, 200, 1, 3, 2]
# nums = [-1,1,0]
# nums = [1,2,0,1]
print(Solution().longestConsecutive(nums))