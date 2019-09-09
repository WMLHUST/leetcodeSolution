class Solution:

    #关键点：1.倒序遍历；2. 遍历的时候顺便排序，从而对下一个要遍历的数，只需查找在排序后的数组中的位置
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def binnarySearch(nums_ordered, cur):
            if len(nums_ordered) == 0:
                return 0

            left = 0
            right = len(nums_ordered) - 1
            if cur <= nums_ordered[left]:
                return 0
            if cur > nums_ordered[right]:
                return right + 1

            mid = (left + right) // 2
            while left < right - 1:
                if cur <= nums_ordered[mid]:
                    right = mid
                elif cur > nums_ordered[mid]:
                    left = mid

                mid = (left + right) // 2

            return right

        # 从后往前，对已经过的进行排序
        res = []
        seen_ordered = []
        for i in range(len(nums)-1, -1, -1):

            # 二分搜索ans的位置
            tmp_res = binnarySearch(seen_ordered, nums[i])
            res.insert(0, tmp_res)
            seen_ordered.insert(tmp_res, nums[i])

        return res

nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
print(Solution().countSmaller(nums))