class Solution:

    # 这个会修改源数组，其实不符合要求
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while True:
            if nums[i] == i:
                i += 1
                continue

            if nums[nums[i]] == nums[i]:
                return nums[i]
            else:
                tmp = nums[i]
                nums[i] = nums[tmp]
                nums[tmp] = tmp

    # 这个也机智，但是涉及到大数，可能会溢出
    def findDuplicate2(self, nums):
        s = set(nums)
        coun = len(nums) - len(s)
        return int((sum(nums) - sum(s)) / coun)

    def findDuplicate3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        slow = nums[0]
        fast = nums[nums[0]]
        while (slow != fast):
            print("slow:{}, numSlow:{}; fast:{}, numFast:{}, num[num[Fast]]:{}".format(slow, nums[slow], fast, nums[fast], nums[nums[fast]]))
            slow = nums[slow]
            fast = nums[nums[fast]]  # fast每次跳两跳，相当于p.next.next b
        fast = 0
        while (slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        return slow

nums = [3,1,3,4,2]
print(Solution().findDuplicate3(nums))