import functools

class Solution:

    # 先排序，h从高到底，h相等时，k从低到高
    # 依次按照(h, k)中的k，插入数组。由于插入时h是从高到低插入的，因此当插入第i个(hi,ki)时，结果数组里的h都比他大，未插入的数组里的h都比它小。
    # 由于ki代表它前面有多少比它高的，而比它高的都已经在结果数组里，因此直接插入到此时结果数组的ki位置即可。（后面进来的不会有影响，因为h都比它小，不会影响k）
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        def custom_key(a, b):
            if a[0] > b[0]:
                return 1
            elif a[0] < b[0]:
                return -1
            else:
                if a[1]<b[1]:
                    return 1
                elif a[1]>b[1]:
                    return -1
                else:
                    return 0

        people.sort(key=functools.cmp_to_key(custom_key), reverse=True)
        print(people)

        res = []
        for i in range(len(people)):
            index = people[i][1]
            res.insert(index, people[i])

        print(res)

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
Solution().reconstructQueue(people)