# coding: utf-8

# 总之想办法减少，确定一个柱子左右边界所需的时间
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s = []
        max_area = 0

        i = 0
        while i < len(heights):
            if len(s)==0 or heights[s[-1]] <= heights[i]:
                # 递增的入栈
                s.append(i)
                i += 1
            else:
                tp = s.pop()
                # tp出栈，出栈时才会计算对应的矩形面积
                # 计算tp对应的矩形面积，tp~i-1 索引的height一定>heights[tp]，不然早在之前遍历时就pop了,
                # 栈里除tp之外的下一个 ~ tp之间的height一定>height[tp]，因为元素在入栈时，总会把栈顶>自己的都出栈掉
                area_with_top = heights[tp] * (i if len(s)==0 else (i-s[-1]-1))
                max_area = max(area_with_top, max_area)

        # 最后剩下的是高度纯递增的，因此宽度都等于 当前高度 * i-s[-1]
        # 剩下的最后一个数很特殊，一定是最小值，因此直接乘以数组长度
        while len(s)>0:
            tp = s.pop()
            area_with_top = heights[tp] * (i if len(s)==0 else (i-s[-1]-1))
            max_area = max(area_with_top, max_area)

        return max_area

heights = [4,5,6,2]
print(Solution().largestRectangleArea(heights))