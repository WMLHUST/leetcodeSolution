class Solution(object):
    def topKFrequent(self, nums, kMax):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt_dict = {}
        for item in nums:
            cnt_dict[item] = cnt_dict.get(item, 0) + 1

        # 从计数中选出频率前K大的num
        # 长度为，频率的最大值，最多所有num相等，占用空间O(N), 时间O(N)
        # 或者用堆，堆空间只用kMax，空间O(kMax)，时间O(N)
        freq_list = [[] for _ in range(len(nums)+1)]
        for k, v in cnt_dict.items():
            freq_list[v].append(k)

        # 加一个空list，并不会导致res变长。
        res = []
        for item in freq_list[::-1]:
            res += item

        return res[:kMax]

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))