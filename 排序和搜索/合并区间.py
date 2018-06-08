# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: x.start)

        res = []
        left = intervals[0].start
        right = intervals[0].end
        for i in range(1, len(intervals)):
            if right >= intervals[i].start:
                if right < intervals[i].end:
                    right = intervals[i].end

            if right < intervals[i].start:
                res.append(Interval(left, right))
                left = intervals[i].start
                right = intervals[i].end

        res.append([left, right])
        return res




