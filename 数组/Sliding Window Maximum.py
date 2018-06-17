class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        win_queue = []
        res = []
        for i in range(0, len(nums)):

            # 删掉不在窗口内的
            if len(win_queue)>0 and win_queue[0] < i-k+1:
                del win_queue[0]

            next_in = nums[i]
            # 删除队列结尾比next_in小的，因为这些数已经没用，这是个降序的队列
            # 如果当前的最大值滑出窗口，那么最大值是next_in。如果next_in是最大，那么队列会只剩它一个
            while True:
                if len(win_queue)==0 or nums[win_queue[-1]] >= next_in:
                    win_queue.append(i)
                    break
                else:
                    del win_queue[-1]

            # 凑够k个才输出
            if i+1>=k:
                res.append(nums[win_queue[0]])

        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3

# nums = [1]
# k = 1
print(Solution().maxSlidingWindow(nums, k))