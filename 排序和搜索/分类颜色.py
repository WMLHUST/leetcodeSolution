class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums)-1
        while j<=k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                continue

            if nums[j] == 1:
                j += 1
                continue

            if nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
                continue

    def sortColors2(self, nums):
        i = -1
        j = -1
        k = -1

        for m in range(len(nums)):
            if nums[m]==0:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1
                i += 1
                nums[i] = 0

            elif nums[m] == 1:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1

            else:
                k += 1
                nums[k] = 2


    # 三路划分，非常经典。搜索荷兰国旗问题
    #
    def sortColor3(self, nums):
        i = 0       #下一个0的位置，i左边都是0
        j = len(nums)-1     #下一个2的位置，最右边是2
        c = 0       #当前位置
        while c <= j:
            # 遇到0就跟i交换，然后i指向下一个0的位置，i左边都是0
            if nums[c] < 1:
                nums[c], nums[i] = nums[i], nums[c]
                c += 1
                i += 1

            elif nums[c] == 1:
                c += 1

            # 遇到2就跟j交换，j指向下一个2的位置，j右边都是2
            elif nums[c] > 1:
                nums[c], nums[j] = nums[j], nums[c]
                j = j - 1

nums = [2, 0, 2, 2, 1, 1, 1, 0]
nums = [2, 0, 1]
Solution().sortColor3(nums)
print(nums)

