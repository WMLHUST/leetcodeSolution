# coding: utf-8
import math


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        begin = -1
        buf = -1
        i=0 #记录交换次数

        begin = 0
        buf = nums[0]
        nextP = 0
        while True:
            nextP = nextP + k
            if nextP > n-1:
                nextP = nextP % n

            if i == n-1:
                nums[begin] = buf
                break

            if nextP!=begin:
                # 正常情况，执行交换
                tmp = buf
                buf = nums[nextP]
                nums[nextP] = tmp
                i = i+1
                # print("nums:{}, buf:{}".format(nums, buf))
            # 有可能在结束前跳成死循环，判断该情况
            else:
                nums[begin] = buf
                i = i+1
                begin += 1
                buf = nums[begin]
                nextP = begin

if __name__=='__main__':
    s = Solution()
    nums = [1,2,3]
    k = 2
    s.rotate(nums=nums, k=k)
    print("res:{}".format(nums))