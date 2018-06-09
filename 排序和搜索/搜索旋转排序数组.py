class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def searchDo(nums, left, right):
            mid = (left+right)//2

            if nums[mid] == target:
                return mid

            if left+1 == right:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                else:
                    return -1

            # 先区分是在哪一段上，再在更小的区间上递归搜索
            if nums[0] < nums[mid]:
                # 左段
                if nums[mid]<target:
                    return searchDo(nums, mid, right)
                else:
                    if nums[left] <= target:
                        return searchDo(nums, left, mid)
                    else:
                        return searchDo(nums, mid, right)

            if nums[right] > nums[mid]:
                # 右段
                if nums[mid]<target:
                    if nums[right] >= target:
                        return searchDo(nums, mid, right)
                    else:
                        return searchDo(nums, left, mid)
                else:
                    return searchDo(nums, left, mid)

        if len(nums)==0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0]==target else -1
        return searchDo(nums, 0, len(nums)-1)

nums = [4,5,6,7,0,1,2]
target = 3
print(Solution().search(nums, target))