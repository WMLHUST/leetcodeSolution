import bisect

# 正确的解法应该是用一个最大堆，最小堆，每次插入O(log(n))，每次计算O(1)
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        index = bisect.bisect_left(self.nums, num)
        self.nums.insert(index, num)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.nums)
        if n%2==0:
            return float((self.nums[n//2-1] + self.nums[n//2]) / 2)
        else:
            return float(self.nums[n//2])

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.nums)
param_2 = obj.findMedian()
print(param_2)