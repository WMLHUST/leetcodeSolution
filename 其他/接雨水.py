class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # max_i = 0
        # for i in range(1, len(height)):
        #     if height[i] > height[max_i]:
        #         max_i = i
        #
        # left_i = 0
        # right_i = len(height)-1
        #
        # while left_i<=right_i:
        #     for i in range(left_i, len(height)):
        if len(height) <= 2:
            return 0

        max = -1
        maxInd = 0
        for i in range(len(height)):
            if height[i] > max:
                max = height[i]
                maxInd = i

        area = 0
        root = height[0]
        for i in range(maxInd):
            if root < height[i]:
                root = height[i]
            else:
                area += root - height[i]

        i = len(height)-1
        root = height[len(height)-1]
        for i in range(len(height)-1, maxInd, -1):
            if root < height[i]:
                root = height[i]
            else:
                area += (root - height[i])

        return area;

height = [0,1,0,2,1,0,1,3,1,3,2,1,2,1]
print(Solution().trap(height))

