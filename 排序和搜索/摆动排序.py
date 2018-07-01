class Solution:
    # 1. 选个中位数
    # 2. 前半部分选一个、后半部分选一个
    # 优点：减少了不必要的对全体num进行排序。而只需部分排序
    def wiggleSort(self, nums):

        # 自己的findKth函数没有sort快.....
        n = len(nums)
        nums.sort()
        mid = nums[n//2]
        # mid = self.findKthLargest(nums, n//2)

        # 三路划分了解一下，https://selfboot.cn/2016/09/01/lost_partition/
        i = 0 # 下一个>mid要放的位置，如果此时j>i，则nums[i]一定==mid，因为如果nums[i]!=mid，则j在经过它的时候，就已经跟i/k交换了。
        j = 0
        k = n-1 # 下一个<mid的位置
        while(j<=k):
            print(nums, end='\t')
            print("i={}, j={}, k={}".format(i, j, k))
            # i指向>mid的，在左边
            if nums[j] > mid:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] < mid:
                # k指向<mid的，在右边
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            else:
                # ==mid
                j += 1

        res = nums[:]
        cur = 0
        if (n&1) == 0:
            for i in range(0, n//2):
                nums[cur] = res[n//2+i]
                cur += 1
                nums[cur] = res[i]
                cur += 1
        else:
            for i in range(1, n//2+1):
                # res.append(nums[n // 2 + i])
                # res.append(nums[i])
                nums[cur] = res[n - i]
                cur += 1
                nums[cur] = res[n//2 -i]
                cur += 1
            nums[cur] = res[n//2]
            # res.append(nums[0])
        print("res={}".format(nums))

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]

        cur = nums[0]
        i = 0
        j = len(nums)-1

        while i<j:
            while i<j and nums[j]>cur:
                j -= 1
            if i<j:
                nums[i] = nums[j]
                i += 1

            while i<j and nums[i]<=cur:
                i += 1
            if i<j:
                nums[j] = nums[i]
                j -= 1

        nums[j] = cur
        right_cnt = len(nums) - j - 1
        if right_cnt == k-1:
            return nums[j]

        elif right_cnt >= k:
            return self.findKthLargest(nums[j+1:], k)
        else:
            return self.findKthLargest(nums[:j], k-right_cnt-1)

nums = [2, 3, 2, 1, 3, 5, 6, 3,9]
nums = [1, 5, 1, 1, 6, 4]
nums = [1,1,2,1,2,2,1]
# nums = [5,3,1,2,6,7,8,5,5]

Solution().wiggleSort(nums)