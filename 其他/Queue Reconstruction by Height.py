import functools

class Solution:

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