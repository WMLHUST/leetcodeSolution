class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        if pow(3, 19) % n == 0:
            return True
        else:
            return False