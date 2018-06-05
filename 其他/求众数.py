class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=1
        cur=nums[0]
        for i in nums[1:]:
            if i==cur:
                cnt+=1
            else:
                cnt -= 1
                if cnt == 0:
                    cur = i
                    cnt = 1
        return cur