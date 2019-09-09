class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res_dict = {}
        for item in strs:
            key = str(sorted(item))
            res_dict[key] = res_dict.get(key, []) + [item]

        return list(res_dict.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))