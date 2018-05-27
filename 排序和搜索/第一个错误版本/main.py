# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isBadVersion(version):
            pass

        left = 1
        right = n

        while True:
            cur = (left + right) // 2

            if isBadVersion(cur):
                right = cur
            else:
                left = cur+1

            if left == right:
                return left