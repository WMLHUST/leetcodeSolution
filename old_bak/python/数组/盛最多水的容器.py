class Solution:

    # 两个指针一左一右，每次计算后，低的那边向中间移动，直到一个比它高
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        if l==r:
            return 0

        res = 0
        while l<r:
            res = max(min(height[l], height[r]) * (r-l), res)

            if height[l]<height[r]:
                while l<r and height[l+1]<height[l]:
                    l += 1
                l = l+1
            else:
                while l<=r and height[r-1]<height[r]:
                    r -= 1
                r = r-1
        return res

height = [1,2,4,3]
print(Solution().maxArea(height))