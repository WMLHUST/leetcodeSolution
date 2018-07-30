# coding: utf-8
# Definition for a point.

# 吐血，这题真折腾。。
# 分步骤来，好好想想原理，一条直线：k&b或 一个固定的点&斜率
# 要注意两点重合的情况。

class Solution:

    def maxPoints(self, points):
        n = len(points)
        if n==0:
            return 0
        if n==1:
            return 1

        def gcd(a, b):
            if b==0:
                return a
            else:
                return gcd(b, a%b)

        res = 0
        for i in range(0, n):
            dup = 0
            k_dict = {}

            # 遍历之后的节点，只根据斜率计数即可（因为默认已经经过了点i，因此再加上斜率可以唯一确定一条直线）
            for j in range(i+1, n):
                # 特殊情况，重合的点
                if points[j].x==points[i].x and points[j].y==points[i].y:
                    dup += 1
                    continue

                k_tmp = None
                if points[j].x != points[i].x:

                    # 需要注意，保存斜率的时候，小数可能是无穷的，所以最好用最简分数的形式。。求最大公约数的公式复习下
                    delta_x = (points[i].x-points[j].x)
                    delta_y = (points[i].y-points[j].y)
                    max_gcd = gcd(delta_x, delta_y)
                    k_tmp = ((points[i].y-points[j].y)/max_gcd, (points[i].x-points[j].x)/max_gcd)

                # 对于斜率无穷大的，会用None来表示
                k_dict[k_tmp] = k_dict.get(k_tmp, 0) + 1

            res = max(dup if len(k_dict.values())==0 else (max(k_dict.values()) + dup), res)

        return res+1

nums = [[0,-1],[0,3],[0,-4],[0,-2],[0,-4],[0,0],[0,0],[0,1],[0,-2],[0,4]]
nums = [[0,0],[94911151,94911150],[94911152,94911151]]
nums = [[1,1],[2,2],[3,3]]
points = []
for item in nums:
    points.append(Point(item[0], item[1]))

print(Solution().maxPoints(points))

